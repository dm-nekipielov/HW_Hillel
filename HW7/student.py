from HW7.utils.db_exequtor import execute_query
from person import Person


class Student(Person):
    _table = "students"
    _role = "Student"

    def __init__(self, first_name, last_name, birthdate):
        super().__init__(first_name, last_name, birthdate)
        self.group_id = None
        if not self._is_exist():
            self._add_to_db()

    def get_student_info(self):
        query = f"""SELECT *
                    FROM students
                    WHERE first_name='{self.first_name}' AND last_name='{self.last_name}'"""
        return execute_query(query)

    def add_to_group(self, group_id):
        self.group_id = group_id
        query = f"""UPDATE {self._table} 
                    SET group_id={group_id} 
                    WHERE first_name='{self.first_name}' AND last_name='{self.last_name}'"""
        execute_query(query)

    def _add_to_db(self):
        query = f"""INSERT INTO {self._table} (first_name, last_name, birthdate)
                    VALUES ('{self.first_name}', '{self.last_name}', '{self.birthdate}')"""
        execute_query(query)


a = Student('hgj', 'cvcv', "25.07.2000")

# s.add_to_db()
print(*a.get_student_info())
# print(a._is_exist())
# print(s.initialization_student())
