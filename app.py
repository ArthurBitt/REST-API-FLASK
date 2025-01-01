from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)


class Users(Resource):
    @staticmethod
    def get():
        return {'message': ' user 1 '}


class User(Resource):
    @staticmethod
    def post():
        return {'message': ' teste '}

    @staticmethod
    def get(cpf):
        return {'message': ' CPF'}


api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/user/<string:cpf>')

if __name__ == '__main__':
    app.run(debug=True)
