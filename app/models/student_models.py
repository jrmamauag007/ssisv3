from app import mysql

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

        cursor.execute("INSERT INTO Students (id, firstname, lastname, studentyear, gender, coursecode, photo_url) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s )",
                       (student_data['id'], student_data['firstname'], student_data['lastname'],
                        student_data['studentyear'], student_data['gender'], student_data['coursecode'],student_data['image_url']))

        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def update_student(cls, student_data):
        connection = mysql.connection
        cursor = connection.cursor()

        cursor.execute("UPDATE Students SET firstname = %s, lastname = %s, studentyear = %s, "
                       "gender = %s, coursecode = %s, photo_url = %s WHERE id = %s",
                       (student_data['firstname'], student_data['lastname'], student_data['studentyear'],
                        student_data['gender'], student_data['coursecode'],student_data['image_url'], student_data['id']))

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

    def associate_image_url(cls, image_url, student_id):
        connection = mysql.connection
        cursor = connection.cursor()

        try:
            # Define the SQL query to update the student's profile_picture_url
            update_query = "UPDATE Students SET photo_url = %s WHERE id = %s"
            
            # Execute the query with the image URL and student ID
            cursor.execute(update_query, (image_url, student_id))
            
            connection.commit()

        except Exception as e:
            # Handle any errors that may occur during the update
            connection.rollback()
            raise e
        finally:
            cursor.close()

    @classmethod
    def get_student_image_url(cls, student_id):
        connection = mysql.connection
        cursor = connection.cursor()

        try:
            # Get Student Image Url
            query = "SELECT photo_url FROM Students WHERE id = %s"
            cursor.execute(query, (student_id,))
            result = cursor.fetchone()
            connection.commit()

            if result:
                return result[0]
            else:
                return None

        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cursor.close()