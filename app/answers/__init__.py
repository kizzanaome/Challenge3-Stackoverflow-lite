from flask import Blueprint
from flask_restful import Api
# from . import views
from .views import answer_details


answers = Blueprint('answers',__name__, url_prefix='/api/v1')
answer_api =Api(answers)

answer_api.add_resource(answer_details, '/questions/<int:qstn_id>/answers')
# answer_api.add_resource(Update ,'/questions/<int:qstn_id>/answers/<int:ans_id>')












