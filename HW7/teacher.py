from person import Person
from utils.db_exequtor import execute_query


class Teacher(Person):
    _table = "teachers"

    def __init__(self, first_name, last_name, birthdate):
        super().__init__(first_name, last_name, birthdate)
        self.group_id = None
        if not self._is_exist():
            self._add_to_db()

    def assign_to_group(self, group_id):
        self.group_id = group_id
        query = f"""UPDATE {self._table} 
                    SET group_id={group_id} 
                    WHERE first_name='{self.first_name}' AND last_name='{self.last_name}'"""
        execute_query(query)


s = Teacher('Koney', 'Smitt', "25.07.2000")
print(s.__str__())
