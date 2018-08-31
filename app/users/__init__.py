from flask import Blueprint
from flask_restful import Api
from ..users.veiws import Register,Login


users = Blueprint('users',__name__, url_prefix='/api/v1')

        
user_api =Api(users)

user_api.add_resource(Register, '/auth/signup')
user_api.add_resource(Login, '/auth/login')




