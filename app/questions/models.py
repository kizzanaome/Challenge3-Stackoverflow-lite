from flask_restful import Api, abort,Resource
from flask import Flask
from ..questions import database
import psycopg2
import psycopg2.extras as naome

database = database.Database()

"""question class"""

class Question():
    """ The class "constructor" - It's actually an initializer """
    def __init__(self, user_id, qstn_title, description):
        self.user_id=user_id
        self.qstn_title =qstn_title
        self.description =description
        
        


    def create_question(self):
        """
            methos creates a question
        """
        conn = None                    
        conn = database.databaseconnections()
        cursor =conn.cursor()
        Sql = "INSERT INTO questions(user_id,qstn_title, description) VALUES( %s,%s,%s)" 
        data = (self.user_id, self.qstn_title, self.description)
        cursor.execute(Sql, data)
        cursor.close()
        conn.commit()
        return True
        
    @staticmethod
    def fetch_all_questions():
        try:            
            conn= database.databaseconnections()
            cursor =conn.cursor(cursor_factory=naome.RealDictCursor)
        
            Sql = ("SELECT * FROM questions;") 
            cursor.execute(Sql)   
            rows = cursor.fetchall()                 
            return rows         
        except (Exception, psycopg2.DatabaseError)as Error:
            raise Error
        finally:
            conn.close()

    @staticmethod   
    def find_by_id(qstn_id):
        try:
            conn= database.databaseconnections()
            cursor =conn.cursor(cursor_factory=naome.RealDictCursor)
            
            sql = ("SELECT * FROM questions WHERE qstn_id = '{}'".format(qstn_id))
            cursor.execute(sql)   
            row = cursor.fetchone()  
            return row
        except (Exception, psycopg2.DatabaseError)as Error:
            raise Error
        finally:
            conn.close()
    @staticmethod
    def delete_question(qstn_id):
        try:
            rows_deleted = 0
            conn= database.databaseconnections()
            cursor =conn.cursor(cursor_factory=naome.RealDictCursor)
            
            query = """DELETE FROM questions WHERE qstn_id='{}'""" .format(qstn_id)
            cursor.execute(query)
            conn.commit()
            rows_deleted = cursor.rowcount 
            return rows_deleted

        except (Exception, psycopg2.DatabaseError)as Error:
            raise Error
        finally:
             if conn is not None:
                conn.close() 
         




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








