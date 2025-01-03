from flask import Flask
from flask_restful import Api
from application.db import mongodb
from application.app import Users, User

def create_app(config):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(config)
    mongodb.init_app(app)

    api.add_resource(Users, '/users')
    api.add_resource(User, '/user', '/user/<string:cpf>')

    return app

