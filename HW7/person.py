from datetime import date, datetime

from utils.db_exequtor import execute_query


class Person:
    date_format = "%d.%m.%Y"
    _table = None

    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = datetime.strptime(birthdate, self.date_format).date()

    def get_age(self):
        current_date = date.today()
        return current_date.year - self.birthdate.year - (
                (current_date.month, current_date.day) < (self.birthdate.month, self.birthdate.day))

    def _add_to_db(self):
        query = f"""INSERT INTO {self._table} (first_name, last_name, birthdate)
                    VALUES ('{self.first_name}', '{self.last_name}', '{self.birthdate}')"""
        execute_query(query)

    def _is_exist(self):
        query = f"""SELECT EXISTS(SELECT * FROM {self._table} 
        WHERE first_name LIKE '{self.first_name}' AND last_name LIKE '{self.last_name}' AND birthdate LIKE '{self.birthdate}')"""
        return bool(execute_query(query)[0][0])
