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
    def get_course_by_code(cls, course_code):
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Courses WHERE coursecode = %s", (course_code,))
        course = cursor.fetchone()

        cursor.close()
        connection.close()

        return course

    @classmethod
    def add_course(cls, course_data):
        connection = mysql.connection
        cursor = connection.cursor()

        cursor.execute("INSERT INTO Courses (coursecode, coursename, collegecode) "
                       "VALUES (%s, %s, %s)",
                       (course_data['coursecode'], course_data['coursename'], course_data['collegecode']))

        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def update_course(cls, course_code, course_data):
        connection = mysql.connection
        cursor = connection.cursor()

        cursor.execute("UPDATE Courses SET coursename = %s, collegecode = %s WHERE coursecode = %s",
                       (course_data['coursename'], course_data['collegecode'], course_code))

        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def delete_course(cls, course_code):
        connection = mysql.connection
        cursor = connection.cursor()

        cursor.execute("DELETE FROM Courses WHERE coursecode = %s", (course_code,))

        connection.commit()
        cursor.close()
        connection.close()
