from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from mongoengine import NotUniqueError

from db import mongodb
from validate_docbr import CPF
from models import UserModel

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'db': 'flask_api',
    'host': 'mongodb',
    'port': 27017,
    'username': 'admin',
    'password': 'admin'
}

mongodb.init_app(app)
_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
    'name', type=str, required=True, help='This field cannot be left blank'
)
_user_parser.add_argument(
    'last_name', type=str, required=True, help='This field cannot be left\
     blank'
)
_user_parser.add_argument(
    'email', type=str, required=True, help='This field cannot be left blank'
)
_user_parser.add_argument(
    'cpf', type=str, required=True, help='This field cannot be left blank'
)
_user_parser.add_argument(
    'birth_date', type=str, required=True, help='This field cannot be \
    left blank'
)


class Users(Resource):
    @staticmethod
    def get():
        return jsonify(UserModel.objects())


class User(Resource):
    @staticmethod
    def post():
        data = _user_parser.parse_args()
        cpf = CPF()
        if not cpf.validate(data.get('cpf')):
            return {'message': 'Invalid CPF'}, 400
        try:
            response = UserModel(**data).save()
            return {'message': 'User %s created successfully' % response.id}
        except NotUniqueError:
            return {'message': 'CPF already registered'}

    @staticmethod
    def get(cpf):
        return {'message': ' CPF'}


api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/user/<string:cpf>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
