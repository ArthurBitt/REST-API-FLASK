import os
import urllib.parse
from dotenv import load_dotenv

load_dotenv()


class DevelopmentConfig:
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': os.getenv('MONGO_DB'),
        'host': os.getenv('MONGO_HOST'),
        'username': os.getenv('MONGO_USER'),
        'password': os.getenv('MONGO_PASS'),
        'uuidRepresentation': 'standard'
    }


class ProductionConfig:
    MONGO_USER = os.getenv('MONGO_USER')
    MONGO_PASS = os.getenv('MONGO_PASS')
    MONGO_HOST = os.getenv('MONGO_HOST')
    MONGO_DB = os.getenv('MONGO_DB')

    MONGODB_SETTINGS = {
        'host': 'mongodb+srv://%s:%s@%s/%s?retryWrites=true&w=majority&\
appName=cluster-flask-rest-api' % (
            urllib.parse.quote_plus(MONGO_USER),
            urllib.parse.quote_plus(MONGO_PASS),
            urllib.parse.quote_plus(MONGO_HOST),
            urllib.parse.quote_plus(MONGO_DB)
        ),
        'uuidRepresentation': 'standard'
    }


class MockConfig:
    DEBUG = True
    TESTING = True
    MONGODB_SETTINGS = {
        'db': 'mock_db',
        'host': 'mongomock://localhost',
        'uuidRepresentation': 'standard'
    }
