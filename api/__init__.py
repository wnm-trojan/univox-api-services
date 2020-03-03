"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Create an application.
"""

import os
from flask import Flask, Response
from core.Middleware import Middleware

# Override response format
class Response(Response):
    charset = 'utf-8'
    default_status = 200
    default_mimetype = 'application/json'

    def __init__(self, response, **kwargs):
        return super(Response, self).__init__(response, **kwargs)

    @classmethod
    def force_type(cls, response, environ=None):
        pass

# Load flask with override format
class Flask(Flask):
    response_class = Response

def create_app():
    app = Flask(__name__)

    # Middleware
    app.wsgi_app = Middleware(app.wsgi_app, prefix='/api/v1')

    # Database
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

    return app
