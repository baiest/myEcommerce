from flask import Blueprint, request, jsonify
from database.sql import *

users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/', methods=['GET'])
def get_users():
    return jsonify(select('users'))