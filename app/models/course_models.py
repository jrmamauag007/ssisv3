# app/models/course_models.py

from app import mysql

class CourseModel:

    @classmethod
    def get_courses(cls):
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Courses")
        courses = cursor.fetchall()

        cursor.close()
        connection.close()

        return courses
    
    @classmethod
    def add_course(cls, course_data):
        connection = mysql.connection
        cursor = connection.cursor()

        try:
            insert_query = "INSERT INTO Courses (coursecode, coursename,collegecode) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (course_data['coursecode'], course_data['coursename'],course_data['collegecode']))
            connection.commit()

        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cursor.close()

    @classmethod
    def update_course(cls, course_code, course_data):
        connection = mysql.connection
        cursor = connection.cursor()

        try:
            update_query = "UPDATE Courses SET coursename = %s WHERE coursecode = %s"
            cursor.execute(update_query, (course_data['coursename'], course_code))
            connection.commit()

        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cursor.close()

    @classmethod
    def delete_course(cls, course_code):
        connection = mysql.connection
        cursor = connection.cursor()
        
        try:
            delete_query = "DELETE FROM Courses WHERE coursecode = %s"
            cursor.execute(delete_query, (course_code,))
            connection.commit()
            return True

        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cursor.close()
