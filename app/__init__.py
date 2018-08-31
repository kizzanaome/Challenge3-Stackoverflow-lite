from flask import Flask, url_for, redirect
from instance.config import app_config

def create_app(config_name):
    """create app function loads the correct 
       configurations from the config.py given the configuration name
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    """
    Registering blueprints

    """
    app.config["JWT_SECRET_KEY"] = "k-i-z-z-a-n-a-o-m-e"
    from flask_jwt_extended import JWTManager
    jwt = JWTManager(app)

    from .questions import questions as questions_blueprint
    app.register_blueprint(questions_blueprint)

    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint)
    
    from .answers import answers as answers_blueprint
    app.register_blueprint(answers_blueprint)
    

    return app
    


