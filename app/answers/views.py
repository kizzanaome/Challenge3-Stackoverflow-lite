from flask_restful import Resource,Api,abort,reqparse
from datetime import date
from flask import Flask , jsonify, make_response,request,json
from app.answers.models import Replytoquestion
import psycopg2
from flask_restful import reqparse,abort 
from flask_jwt_extended import jwt_required, get_jwt_identity

class answer_details(Resource): 
    @jwt_required
    def post(self, qstn_id):
        """This method adds an answer"""
    
        parser = reqparse.RequestParser()
        parser.add_argument("ans_body")
        parser.add_argument("most_correct")
        args = parser.parse_args()  
        user_id = get_jwt_identity()        
        answer = Replytoquestion(user_id,qstn_id,args["ans_body"],args['most_correct'])
        anser = answer.answer_question()
        if anser:
            return {"massage": "Your answer has been sent" },201
        return {"msg": "Sorry we couldn't create the anser"}, 500

class Update(Resource):
    def put(self,qstn_id,ans_id):
        parser = reqparse.RequestParser()
        parser.add_argument("ans_body")
        parser.parse_args()     
        data = request.get_json()
        answer = data.get("answer")
        print(answer)
        ans_body=data['ans_body']
        Replytoquestion.edit_answer(ans_id,ans_body)
        return {'message': 'question updated '},201

    
        








        
            