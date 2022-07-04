import csv
import json
import random
from http import HTTPStatus

import requests
from faker import Faker
from flask import Flask, jsonify
from webargs import validate, fields
from webargs.flaskparser import use_kwargs

from HW3.currencies import currencies_list

app = Flask(__name__)

fake = Faker()


@app.errorhandler(HTTPStatus.BAD_REQUEST)
@app.errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
def error_hendler(error):
    headers = error.data.get("headers", None)
    messages = error.data.get("messages", ["Invalid request."])

    return jsonify(
        {
            "errors": messages
        },
        error.code,
        headers
    ) if headers else jsonify(
        {
            "errors": messages
        },
        error.code
    )


@app.route("/students")
@use_kwargs(
    {
        "quantity": fields.Int(
            missing=10,
            validate=[validate.Range(min=1, max=1000)]
        )
    },
    location="query"
)
def generate_students(quantity):
    students_list = []
    for i in range(int(quantity)):
        students_list.append(
            dict(First_name=fake.first_name(),
                 Last_name=fake.last_name(),
                 Email=fake.unique.email(),
                 Password=fake.password(length=random.randint(10, 25)),
                 Birthday=str(fake.date_of_birth(minimum_age=18, maximum_age=45))))
    json_string = json.dumps(students_list)

    with open("students.csv", "w", newline="") as f:
        fieldnames = ["First_name", "Last_name", "Email", "Password", "Birthday"]
        writer = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students_list)
    # Пробував повенути jsonify(students_list) -- ключі сортуються по алфавіту, а не так я я їх передавав в dict.
    # Тобто спочатку Birthday, Email і т.д.
    # Ні на що не впливаеє, але не гарно. Тому знайшов таке рішення.
    return json_string, 200, {"Content-Type": "application/json"}


@app.route("/bitcoin_rate")
@use_kwargs(
    {
        "count": fields.Int(
            missing=1,
            validate=[validate.Range(min=1)]
        ),
        "currency": fields.Str(
            missing="USD",
            validate=[validate.OneOf(currencies_list)]
        )
    },
    location="query"
)
def get_bitcoin_value(count, currency):
    response = requests.get(f"https://bitpay.com/api/rates/{currency}").json()
    currency_symbols = requests.get("https://bitpay.com/currencies").json()

    rate = round(response["rate"] * int(count), 2)

    symbol = ''
    for i in currency_symbols["data"]:
        if i["code"] != currency.upper():
            continue
        symbol = i["symbol"]

    return f"{count} BTC == {rate} {symbol}"


if __name__ == '__main__':
    app.run(debug=True)
