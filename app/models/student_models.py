from app import mysql
import cloudinary
import cloudinary.uploader

class StudentModel:

    @classmethod
    def get_students(cls):
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Students")
        students = cursor.fetchall()

        cursor.close()

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
    def update_student(cls, student_data):
        connection = mysql.connection
        cursor = connection.cursor()

        cursor.execute("UPDATE Students SET firstname = %s, lastname = %s, studentyear = %s, "
                       "gender = %s, coursecode = %s WHERE id = %s",
                       (student_data['firstname'], student_data['lastname'], student_data['studentyear'],
                        student_data['gender'], student_data['coursecode'], student_data['id']))

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

    @classmethod
    def get_student_with_photo(cls, student_id):
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT *, photo_url FROM Students WHERE id = %s", (student_id,))
        student = cursor.fetchone()

        cursor.close()
        connection.close()

        return student

    @classmethod
    def update_student_photo(cls, student_id, photo_url):
        connection = mysql.connection
        cursor = connection.cursor()

        cursor.execute("UPDATE Students SET photo_url = %s WHERE id = %s", (photo_url, student_id))

        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def delete_student_photo(cls, student_id):
        connection = mysql.connection
        cursor = connection.cursor()

        cursor.execute("UPDATE Students SET photo_url = NULL WHERE id = %s", (student_id,))

        connection.commit()
        cursor.close()
        connection.close()