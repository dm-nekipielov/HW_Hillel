from datetime import datetime

from utils.db_exequtor import execute_query


class Group:
    date_format = "%d.%m.%Y"

    def __init__(self, course_name, start_date):
        self.course_name = course_name
        self.start_date = datetime.strptime(start_date, self.date_format).date()
        self.group_name = f"{course_name.replace(' ', '_')}_({start_date})"

    def add_to_db(self):
        query = f"""INSERT INTO 'groups' (course_name, start_date, group_name) 
                    VALUES ('{self.course_name}', '{self.start_date}', '{self.group_name}')"""
        execute_query(query)

    def get_group_id(self):
        query = f"""SELECT group_id FROM groups
                    WHERE group_name='{self.group_name}'"""
        return execute_query(query)[0][0]

    @classmethod
    def get_students(cls, group_id):
        query = f"""SELECT students.student_id, students.first_name, students.last_name FROM students
                    JOIN groups ON students.group_id = groups.group_id
                    WHERE students.group_id='{group_id}'"""
        return execute_query(query)


