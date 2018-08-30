from flask_restful import Api, abort,Resource
from flask import Flask
from ..questions import database
import psycopg2

database = database.Database()

"""we first create empty lists"""

                
class Replytoquestion:
    def __init__(self,user_id, qstn_id, ans_body,most_correct):
        self.user_id = user_id
        self.qstn_id = qstn_id
        self.ans_body = ans_body
        self.most_correct = most_correct
    

    def answer_question(self):
        """
            methos creates a question
        """
        conn = None                    
        conn = database.databaseconnections()
        cursor =conn.cursor()
        try:
            Sql = "INSERT INTO answers(qstn_id, user_id,ans_body, most_correct) VALUES( %s,%s,%s,%s)" 
            data = ( self.qstn_id,self.user_id, self.ans_body,self.most_correct)
            cursor.execute(Sql, data)
            cursor.close()
            conn.commit()
            return True
        except (Exception, psycopg2.DatabaseError)as Error:
            raise Error
        finally:
            conn.close()

    def edit_answer(self, ans_id, ans_body):
        conn = None                    
        conn = database.databaseconnections()
        cursor =conn.cursor()
        try:
            Sql = "UPDATE answers SET ans_body ='{}' WHERE ans_id ={}" .format(ans_body, ans_id)
            cursor.execute(Sql)
            cursor.close()
            conn.commit()
            return True
        except (Exception, psycopg2.DatabaseError)as Error:
            raise Error
      

            
       