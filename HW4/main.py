from flask import Flask, render_template
from webargs import fields
from webargs.flaskparser import use_kwargs

from db_executor import execute_query

app = Flask(__name__)


@app.route("/order_price")
@use_kwargs(
    {
        "country": fields.Str(
            required=False,
            load_default=None,
        )
    },
    location="query"
)
def order_price(country):
    query = """
            SELECT SUM(invoice_items.UnitPrice * invoice_items.Quantity) AS Sales, invoices.BillingCountry AS Country
            FROM invoices
            INNER JOIN invoice_items ON invoice_items.InvoiceId = invoices.InvoiceId
    """
    if country:
        query += f"WHERE Country=='{country}'"
    else:
        query += "GROUP BY invoices.BillingCountry"

    results = execute_query(query)
    return render_template("order_price.html", results=results)


@app.route("/tracks_info")
@use_kwargs(
    {
        "track_ID": fields.Int(
            required=False,
            load_default=None,
        )
    },
    location="query"
)
def get_all_info_about_track(track_ID):
    all_tracks_info_query = """
            SELECT tracks.TrackId, tracks.Name, artists.Name, albums.Title, 
            genres.Name, playlists.Name, tracks.Composer, media_types.Name,
            tracks.Milliseconds, tracks.Bytes, tracks.UnitPrice
            FROM tracks
            JOIN albums ON albums.AlbumId = tracks.AlbumId
            JOIN media_types ON media_types.MediaTypeId = tracks.MediaTypeId
            JOIN genres ON genres.GenreId = tracks.GenreId
            JOIN playlist_track ON playlist_track.TrackId = tracks.TrackId
            JOIN playlists ON playlists.PlaylistId = playlist_track.PlaylistId
            JOIN artists ON artists.ArtistId = albums.ArtistId
    """

    total_hours_query = """
            SELECT ROUND((TOTAL(Milliseconds)/3600000), 2) AS TotalTime 
            FROM tracks
    """

    if track_ID:
        all_tracks_info_query += f"WHERE tracks.TrackId={track_ID} GROUP BY tracks.TrackId"
    else:
        all_tracks_info_query += "GROUP BY tracks.TrackId"

    all_tracks_info = execute_query(all_tracks_info_query)
    total_hours = execute_query(total_hours_query)[0][0]

    return render_template("tracks_info.html", all_tracks_info=all_tracks_info, total_hours=total_hours)


if __name__ == '__main__':
    app.run(debug=True)
