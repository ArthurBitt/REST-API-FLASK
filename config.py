class DevelopmentConfig:
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'flask_api',
        'host': 'mongodb',
        'port': 27017,
        'username': 'admin',
        'password': 'admin'
    }

class ProductionConfig:
    ...