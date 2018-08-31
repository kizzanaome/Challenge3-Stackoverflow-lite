from flask_restful import Resource,Api,abort,reqparse
from datetime import date
from flask import Flask , jsonify, make_response
from app.questions.models import Question
import psycopg2
from flask_restful import reqparse,abort 
from flask_jwt_extended import jwt_required,get_jwt_identity


class Question_Details(Resource): 

    """Method for getting questions"""
    @jwt_required
    def get(self):
        try:
            
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
        current_user = get_jwt_identity()
        parser = reqparse.RequestParser()
       
        parser.add_argument('qstn_title')
        parser.add_argument('description')
        args = parser.parse_args()

        question = Question(current_user, args['qstn_title'], args['description'])
        if question.check_question(args['qstn_title'].strip()):
            return {"msg": "This question has qlready been asked"}, 409

        create_qstn = question.create_question()
        if create_qstn:
            return make_response(jsonify({"massage":"Question has been created"}),201)
        return {"msg": "Sorry we couldn't create that question"}, 500

  
class Singlequestion(Resource):
    """Method for veiwing a single question"""
    @jwt_required
    def get(self, qstn_id):         
        if qstn_id:
            qsr = Question.find_by_id(qstn_id)
            ans =Question.anwer(qstn_id)
            print (ans)
            if not qsr:
                return {'msg': "qstn not found "}
            return make_response(jsonify({"question": qsr},{"answer": ans}),200)
            
    
    def delete(self, qstn_id):
        if qstn_id:
            question=Question.delete_question(qstn_id)
            if question < 0:
                return {'msg': "Question not deleted "}
            return make_response(jsonify({"massage":"Your question has been deleted succesfully"}),201)


    

    









        
            