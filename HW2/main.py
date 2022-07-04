import random

import pandas
from faker import Faker
from flask import Flask

fake = Faker()

app = Flask(__name__)


@app.route("/password")
def generate_password() -> str:
    length = random.randint(10, 25)
    password = fake.password(length=length)
    return f"<p>Password: {password}</p>"


@app.route("/average")
def calculate_average() -> str:
    try:
        data = pandas.read_csv("hw.csv")
        average_height = round(data.mean()[" Height(Inches)"], 2)
        average_weight = round(data.mean()[" Weight(Pounds)"], 2)
    except FileNotFoundError:
        return "Не вдалось прочитати файл."
    return f"<p>Average height: {average_height} Inches<br> Average weight: {average_weight} Pounds</p>"


# @app.route("/average")
# def calculate_average() -> str:
#     all_weights = []
#     all_heights = []
#     try:
#         with open("hw.csv") as f:
#             reader = csv.DictReader(f, delimiter=",")
#             for row in reader:
#                 all_heights.append(float(row[" Height(Inches)"]))
#                 all_weights.append(float(row[" Weight(Pounds)"]))
#     except FileNotFoundError:
#         return "Не вдалось прочитати файл."
#     average_height = round((sum(all_heights) / len(all_heights)), 2)
#     average_weight = round((sum(all_weights) / len(all_weights)), 2)
#     return f"<p>Average height: {average_height} Inches<br> Average weight: {average_weight} Pounds</p>"


if __name__ == "__main__":
    app.run(debug=True)
