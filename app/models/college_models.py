from app import mysql

class CollegeModel:

    @classmethod
    def get_colleges(cls):
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Colleges")
        colleges = cursor.fetchall()

        cursor.close()
        connection.close()

        return colleges
    @classmethod
    def get_college_by_code(cls,collegecode):
        connection = mysql.connection
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Colleges WHERE collegecode = %s", (collegecode,))
        college = cursor.fetchone()

        cursor.close()
        connection.close()

        return college
    @classmethod
    def add_college(cls,collegecode, collegename):
        connection = mysql.connection
        cursor = connection.cursor()

        cursor.execute("INSERT INTO Colleges (collegecode, collegename) VALUES (%s, %s)", (collegecode, collegename))

        connection.commit()
        cursor.close()
        connection.close()
    @classmethod
    def update_college(cls,collegecode, collegename):
        connection = mysql.connection
        cursor = connection.cursor()

        cursor.execute("UPDATE Colleges SET collegename = %s WHERE collegecode = %s", (collegename, collegecode))

        connection.commit()
        cursor.close()
        connection.close()
    @classmethod
    def delete_college(cls,collegecode):
        connection = mysql.connection
        cursor = connection.cursor()

        cursor.execute("DELETE FROM Colleges WHERE collegecode = %s", (collegecode,))

        connection.commit()
        cursor.close()
        connection.close()
