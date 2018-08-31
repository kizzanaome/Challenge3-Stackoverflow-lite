from flask_restful import Api, abort, Resource
from flask import Flask
from ..questions import database
import psycopg2

database = database.Database()

"""User class"""
class User:
    """ This is a class "constructor" - It's actually an initializer """

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    # def password_is_valid(self, password):

    #     """
    #     Checks the password against it's hash to validates the user's password

    #     """
    #     return check_password_hash(self.password, password)

    @staticmethod
    def fetchsingle(username,password):
        conn = database.databaseconnections()
        cursor = conn.cursor()
        print(cursor)
        try:
            cursor.execute("SELECT * FROM users WHERE username=%s and password=%s",[username,password])
            return cursor.fetchone()
        except Exception as e:
            raise e

    def insert_data(self):
        """Adds a new record to the database"""
        conn = database.databaseconnections()
        cursor = conn.cursor()
        print(cursor)
        Sql = "INSERT INTO users(username,email, password) VALUES( %s,%s,%s)"
        data = (self.username, self.email, self.password)
        cursor.execute(Sql, data)

        conn.commit()
        return True
    
    def check_username(self,username):
        conn = database.databaseconnections()
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username=%s"
        cursor.execute(query, (username,))
        username = cursor.fetchone()
        if username:
            return True
        return False

    