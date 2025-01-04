from flask import jsonify
from flask_restful import Resource, reqparse
from mongoengine import NotUniqueError

from validate_docbr import CPF
from application.models import UserModel


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
            return (
                {'message': 'User %s created successfully' % response.id}, 201
            )
        except NotUniqueError:
            return {'message': 'CPF already registered'}, 400

    @staticmethod
    def get(cpf):
        query = UserModel.objects(cpf=cpf).first()
        if query:
            return jsonify(query)
        return {'message': 'User not found'}, 404
