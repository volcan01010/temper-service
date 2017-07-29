import logging
from logging.handlers import RotatingFileHandler
import os

from flask import Flask
from flask_restful import Api


def create_app():
    """ Bootstrap function to initialise the Flask app and config """
    app = Flask(__name__)

    env = os.getenv('TEMPER_SERVICE_ENV', 'Dev')  # default to Dev if config environment var not set
    app.config.from_object('app.config.{0}Config'.format(env))

    initialise_logger(app)
    app.logger.debug("Starting temper-service.")

    init_flask_restful_routes(app)

    return app


def initialise_logger(app):
    """ Read environment config then initialise a 2MB rotating log """
    log_dir = app.config['LOG_DIR']
    log_level = app.config['LOG_LEVEL']

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    file_handler = RotatingFileHandler(log_dir + '/temper-service.log', 'a', 2 * 1024 * 1024, 3)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

    app.logger.addHandler(file_handler)
    app.logger.setLevel(log_level)


def init_flask_restful_routes(app):
    """
    Define the routes the API exposes using Flask-Restful.  See docs here
    http://flask-restful-cn.readthedocs.org/en/0.3.5/quickstart.html#endpoints
    """
    app.logger.info('Initialising API Routes')
    api = Api(app)

    from app.api.hello_api import HelloAPI, CalcAPI
    from app.api.temper_api import TemperAPI

    api.add_resource(HelloAPI, '/hello')
    api.add_resource(CalcAPI, '/calculate')
    api.add_resource(TemperAPI, '/temper')
