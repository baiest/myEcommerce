from flask import Blueprint
from .Users import users
import os

api = Blueprint('api', __name__, url_prefix='/api')

api.register_blueprint(users)