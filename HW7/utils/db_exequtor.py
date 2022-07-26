import sqlite3


def execute_query(query):
    with sqlite3.connect('my_base.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        records = cursor.fetchall()
    return records
