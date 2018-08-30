from flask_restful import Resource,Api,abort,reqparse
from datetime import date
from flask import Flask , jsonify, make_response
from app.questions.models import Question
import psycopg2
from flask_restful import reqparse,abort 
from flask_jwt_extended import jwt_required


class Question_Details(Resource): 

    """Method for getting questions"""
    @jwt_required
    def get(self):
        try:
            #qstn=Question()
            qstns = Question.fetch_all_questions()
            print(qstns)
            if qstns ==True:
                return {"msg": " There are no questions at the momnet"}, 200 
            return make_response(jsonify({"questions": qstns}),200)
            
        except (Exception, psycopg2.DatabaseError)as Error:
            print(Error)
           
    @jwt_required
    def post(self):
        """method for posting question"""
        parser = reqparse.RequestParser()
        parser.add_argument('user_id')
        parser.add_argument('qstn_title')
        parser.add_argument('description')
        args = parser.parse_args()
        question = Question(args['user_id'], args['qstn_title'], args['description'])
        create_qstn = question.create_question()
        if create_qstn:
            return make_response(jsonify({"massage":"Question has been created"}),201)
        return {"msg": "Sorry we couldn't create that question"}, 500

  
class Singlequestion(Resource):
    """Method for veiwing a single question"""
    @jwt_required
    def get(self, qstn_id):
        """Method for  get requests"""          
        if qstn_id:
            # qstn = Question(None,qstn_id,None)
            qsr = Question.find_by_id(qstn_id)
            if not qsr:
                return {'msg': "qstn not found "}
            return make_response(jsonify({"question": qsr}),200)
    @jwt_required
    def delete(self, qstn_id):
        if qstn_id:
            question=Question.delete_question(qstn_id)
            if question < 0:
                return {'msg': "Question not deleted "}
            return make_response(jsonify({"massage":"deleted succesfully"}),201)



        

# class Singlequestion(Resource):
#     """Method for veiwing a single question"""
#     def get(self, qstn_id):
#         a_qustn = None
#         for question in question_db:
#             if (question["qstn_id"] == qstn_id):
#                 a_qustn = question
#                 return make_response(jsonify({"question":a_qustn}), 200)
#         return make_response(jsonify({"message":"Question not found"}),404)








        
            