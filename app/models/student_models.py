from app import mysql

class StudentModel:

    @classmethod
    def get_students(cls):
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Students")
        students = cursor.fetchall()

        cursor.close()
        connection.close()

        return students

    @classmethod
    def get_student_by_id(cls, student_id):
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Students WHERE id = %s", (student_id,))
        student = cursor.fetchone()

        cursor.close()
        connection.close()

        return student

    @classmethod
    def add_student(cls, student_data):
        connection = mysql.connection
        cursor = connection.cursor()

        cursor.execute("INSERT INTO Students (id, firstname, lastname, studentyear, gender, coursecode) "
                       "VALUES (%s, %s, %s, %s, %s, %s)",
                       (student_data['id'], student_data['firstname'], student_data['lastname'],
                        student_data['studentyear'], student_data['gender'], student_data['coursecode']))

        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def update_student(cls, student_id, student_data):
        connection = mysql.connection
        cursor = connection.cursor()

        cursor.execute("UPDATE Students SET firstname = %s, lastname = %s, studentyear = %s, "
                       "gender = %s, coursecode = %s WHERE id = %s",
                       (student_data['firstname'], student_data['lastname'], student_data['studentyear'],
                        student_data['gender'], student_data['coursecode'], student_id))

        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def delete_student(cls, student_id):
        connection = mysql.connection
        cursor = connection.cursor()

        cursor.execute("DELETE FROM Students WHERE id = %s", (student_id,))

        connection.commit()
        cursor.close()
        connection.close()
