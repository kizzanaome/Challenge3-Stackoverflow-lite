from flask import Blueprint
from flask_restful import Api
# from . import views
from .views import Question_Details,Singlequestion

qstn=Question_Details()


questions = Blueprint('questions',__name__, url_prefix='/api/v1')
questions_api =Api(questions)

questions_api.add_resource(Question_Details, '/questions')
questions_api.add_resource(Singlequestion, '/questions/<int:qstn_id>')











