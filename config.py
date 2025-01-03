
import os

class DevelopmentConfig:
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': os.getenv('MONGO_DB'),
        'host': os.getenv('MONGO_HOST'),
        'username': os.getenv('MONGO_USER'),
        'password': os.getenv('MONGO_PASS'),
    }


class ProductionConfig:
    ...
