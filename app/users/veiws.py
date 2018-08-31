from flask_restful import reqparse, abort,Resource
from ..users.models import User
from flask import make_response,jsonify
import re
import jwt
from flask_restful import Resource
import psycopg2
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_claims)
import string

class Register(Resource):
    """ function fro registering a user"""
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="The title field can't be empty")
        parser.add_argument('email', type=str, required=True,help="The title field can't be empty")
        parser.add_argument('password',type=str,required=True,help="The title field can't be empty")
        args = parser.parse_args()

        ''' validate data sent '''
    
        if not args['username']:
            return make_response(jsonify({"message":
                                          "Username field is required"}),
                                 401)

        if args['username'].isspace():
            return make_response(jsonify({"message":
                                          "Invalid user input"}),
                                 401)


            
        if not args['email']:
            return make_response(jsonify({"message":
                                          "Email  field is required"}),
                                 401)
        if not args['password']:
            return make_response(jsonify({"message":
                                          "Please enter persword"}),
                                 401)
     

        if len(str(args['password'])) < 4:
             return {'message': 'Your password is too short'}, 400

        if not isinstance(args['username'], str ) or args['username'].isspace() or args['username'] == "" :
            return {"message": 'Invalid userinput Please enter a correct username'}, 406

        if not isinstance(args['password'], str ) or args['password'].isspace() or args['password'] == "":
            return {"message": 'Invalid, Please enter a correct password'}, 406

        if not re.match(r"[a-za-z0-9]+@[a-z]+", args['email']):
            return {'message': 'Invalid email, Please check email'}, 400

        user = User(args['username'], args['email'],args['password'])
        if user.check_username(args['username'].strip()):
            return {"msg": "The user already exists"}, 409
            
        createuser = user.insert_data()
        if createuser:
            return make_response(jsonify({"massage":"user has been created"}),201)
        return {"msg": "Sorry we couldn't create that user"}, 400

class Login(Resource):
       
    def post(self):
        """
        Allows users to login to their accounts

        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password',type=str,required=True)
        args = parser.parse_args()
      
        username1 = User.fetchsingle(args['username'].strip(), args['password'].strip())
        if  username1:
            user_token = {}
            access_token = create_access_token(identity= username1[0]).decode('UTF-8')
            
            user_token["token"] = access_token
            return user_token, 200
        else:
            return {'message':'user not registered'}, 401
        





       

       
