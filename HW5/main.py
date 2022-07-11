import sqlite3
from collections import namedtuple

from flask import Flask
from webargs import validate, fields
from webargs.flaskparser import use_kwargs

app = Flask(__name__)


@app.route("/stats_by_city")
@use_kwargs(
    {
        "genre": fields.Str(
            required=True,
            validate=validate.Regexp("[a-zA-Z\s\W]")
        )
    },
    location="query"
)
def stats_by_city(genre):
    query = f"""
        SELECT BillingCountry, max(count)
        FROM (
        SELECT genres.Name, invoices.BillingCountry, COUNT(invoices.BillingCountry) as count
        FROM genres
        JOIN tracks ON genres.GenreId = tracks.GenreId
        JOIN invoice_items ON tracks.TrackId = invoice_items.TrackId
        JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
        GROUP BY genres.Name, invoices.BillingCountry
        )
        WHERE Name='{genre}'
        """

    country = namedtuple('country', ['name', 'sales'])

    country.name, country.sales = execute_query(query)[0]
    genres_list = execute_query("SELECT Name FROM genres")
    if country.name:
        return f"<p>{genre} most popular in {country.name}.</p>"
    else:
        return f"Incorrect genre.<br> Try one of this:<br> {'<br>'.join(i[0] for i in genres_list)}"


def execute_query(query):
    with sqlite3.connect('../chinook.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        records = cursor.fetchall()
    return records


if __name__ == '__main__':
    app.run(debug=True)
