from flask import Flask, request, abort, current_app, jsonify
from werkzeug.utils import find_modules, import_string
from . import views

def create_app(environment=None):
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    register_blueprints(app)
    return app



def register_blueprints(app):
    for module in find_modules('app.views'):
        app.register_blueprint(import_string(module).app)