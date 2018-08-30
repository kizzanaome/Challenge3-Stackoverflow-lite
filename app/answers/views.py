from flask_restful import Resource,Api,abort,reqparse
from datetime import date
from flask import Flask , jsonify, make_response,request,json
from app.answers.models import Replytoquestion
import psycopg2
from flask_restful import reqparse,abort 

class answer_details(Resource): 

    # """Method for getting questions"""
    # def get(self):
    #     try:
    #         qstn=Question('user_id', 'qstn_title', 'description')
    #         qstns = qstn.fetch_all_questions()
    #         print(qstns)
    #         if qstns ==True:
    #             return {"msg": " There are no questions at the momnet"}, 200 
    #         return make_response(jsonify({"questions": qstns}),200)
            
    #     except (Exception, psycopg2.DatabaseError)as Error:
    #         print(Error)
           


    def post(self, qstn_id):
        """This method adds an answer"""
    
        parser = reqparse.RequestParser()
        parser.add_argument("ans_body")
        parser.add_argument("most_correct")
        args = parser.parse_args()          
        answer = Replytoquestion(None,qstn_id,args["ans_body"],args['most_correct'])
        anser = answer.answer_question()
        if anser:
            return {"massage":"ansers has been creaded"},201
        return {"msg": "Sorry we couldn't create the anser"}, 500

# class Update(Resource):
#     def put(self,ans_body ,ans_id):
#         parser = reqparse.RequestParser()
#         ans_body =parser.add_argument("ans_body")
#         parser.parse_args()     
#         Replytoquestion.edit_answer(ans_body,ans_id)
#         data = request.get(json)
#         ans_body=data['ans_body']
#         return jsonify({'message: question updated '}),201
        


    



        
# class Singlequestion(Resource):
#     """Method for veiwing a single question"""

#     def get(self, qstn_id):
#         """Method for  get requests"""
#         if qstn_id:
#             try:
#                # qstn = Question(None,qstn_id,None)
#                 qsr = Question.find_by_id(qstn_id)
#                 if qsr:
#                     return jsonify({'msg': "qstn not found "}), 404
#                 return jsonify(qsr), 204
#             except Exception as e:
#                 response = {
#                     'message': str(e)
#                 }
#                 return make_response(jsonify(response)), 500



        








        
            