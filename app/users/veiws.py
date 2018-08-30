from flask_restful import reqparse, abort,Resource
from ..users.models import User
from flask import make_response,jsonify
import jwt
from flask_restful import Resource
import psycopg2
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_claims)

class Register(Resource):
    """ function fro registering a user"""
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password',type=str,required=True)
        args = parser.parse_args()

        user = User(args['username'], args['email'],args['password'])
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
        # print(user,args['password'])

        username1 = User.fetchsingle(args['username'], args['password'])
        if  username1:
            user_token = {}
            access_token = create_access_token(identity= args["username"])
            user_token["token"] = access_token
            return {'message':user_token}, 200
        else:
            return {'message':'wrong username or password or user not registered'}, 401
        



       

       
