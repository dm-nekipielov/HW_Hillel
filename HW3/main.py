import csv
import random
from http import HTTPStatus

import requests
from faker import Faker
from flask import Flask, jsonify, abort
from webargs import validate, fields
from webargs.flaskparser import use_kwargs

app = Flask(__name__)

fake = Faker()


@app.errorhandler(HTTPStatus.BAD_REQUEST)
@app.errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
def error_handler(error):
    return jsonify(error=str(error))


@app.route("/students")
@use_kwargs(
    {
        "quantity": fields.Int(
            load_default=10,
            validate=[validate.Range(min=1, max=1000)]
        )
    },
    location="query"
)
def generate_students(quantity):
    students_list = [
        {
            "First_name": fake.first_name(),
            "Last_name": fake.last_name(),
            "Email": fake.unique.email(),
            "Password": fake.password(length=random.randint(10, 25)),
            "Birthday": str(fake.date_of_birth(minimum_age=18, maximum_age=45))
        } for _ in range(quantity)
    ]

    with open("students.csv", "w", newline="") as f:
        fieldnames = ["First_name", "Last_name", "Email", "Password", "Birthday"]
        writer = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students_list)

    app.config.update(JSON_SORT_KEYS=False)

    return jsonify(students_list)


@app.route("/bitcoin_rate")
@use_kwargs(
    {
        "count": fields.Int(
            load_default=1,
            validate=[validate.Range(min=1)]
        ),
        "currency": fields.Str(
            load_default="USD"
        )
    },
    location="query"
)
def get_bitcoin_value(count, currency):
    currency = currency.upper()
    currencies = requests.get("https://bitpay.com/currencies").json()
    currencies = currencies['data']

    available_currency_codes = [currency['code'] for currency in currencies]

    validate_currency(available_currency_codes, currency)

    response = requests.get(f"https://bitpay.com/api/rates/{currency}").json()
    rate = round(response["rate"] * int(count), 2)
    symbol = next(bitpay_currency['symbol'] for bitpay_currency in currencies if bitpay_currency['code'] == currency)

    return f"{count} BTC == {rate} {symbol}"


def validate_currency(available, requested):
    if requested not in available:
        raise abort(400, description=[f'Wrong currency code. Available codes: {available}'])


if __name__ == '__main__':
    app.run(debug=True)
