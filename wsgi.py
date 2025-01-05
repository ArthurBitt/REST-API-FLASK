import config
from application import create_app
import os

if os.environ.get('FLASK_ENV') == 'development':
    config = config.DevelopmentConfig
    app = create_app(config)
else:
    app = create_app(config.ProductionConfig)

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_ENV') == 'development', host='0.0.0.0')