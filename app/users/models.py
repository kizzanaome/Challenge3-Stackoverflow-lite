from flask_restful import Api, abort, Resource
from flask import Flask
from ..questions import database
import psycopg2

database = database.Database()

"""question class"""


class User:
    """ The class "constructor" - It's actually an initializer """

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
            # user = cursor.fetchone()
            # username = user[1]
            # # password = user[3]
            # conn.commit()
            return cursor.fetchone()
        except Exception as e:
            raise e
            # return {"error": "Couldn't get user"}

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

# class Singlequestion(Resource):
#     """Method for veiwing a single question"""
#     def get(self, qstn_id):
#         a_qustn = None
#         for question in question_db:
#             if (question["qstn_id"] == qstn_id):
#                 a_qustn = question
#                 return make_response(jsonify({"question":a_qustn}), 200)
#         return make_response(jsonify({"message":"Question not found"}),404)


# if __name__ == '__main__':
#     qstn =Question('1', '2', 'qstn_title', 'description' )
#     qstn.create_question()
#     qstn.fetch_all_questions()

# class Replytoquestion():
#     def __init__(self, qstn_id, reply):
#         self.qstn_id = qstn_id
#         self.reply = reply

#     def create_answer(self):
#         answer = {
#             "qstn_id": self.qstn_id,
#             "reply": self.reply
#         }

#         answers.append(answer)
#         return answer
