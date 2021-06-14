from flask import Blueprint, request, jsonify
from database.sql import *

users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/')
def get_users():
    return jsonify(select('products'))

@users.route('/<int:id>', methods=['GET'])
def get_users_id(id):
    return f'Hola usuarios {id}'