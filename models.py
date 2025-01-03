from db import mongodb


class UserModel(mongodb.Document):
    name = mongodb.StringField(required=True)
    last_name = mongodb.StringField(required=True)
    cpf = mongodb.StringField(required=True, unique=True)
    email = mongodb.EmailField(required=True)
    birth_date = mongodb.DateField(required=True)
