from flask import Blueprint, request, jsonify
from database.sql import *
from dotenv import dotenv_values
from .Login import token_required
import jwt

_env = dotenv_values('.env')
users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/', methods=['GET'])
def get_users():
    return jsonify(select('users'))

@users.route('/auth', methods=['POST'])
def auth():
    try:
        token = request.headers['token']
        decode_jwt = jwt.decode(token, _env['TOKEN_PASS'], algorithms=["HS256"])
        return jsonify(decode_jwt)
    except jwt.exceptions.InvalidSignatureError as error:
        return jsonify({'error': 'Token invalido'}), 305
    except Exception as error:
        return jsonify({'error': str(error)}), 305
    
@users.route('/cart', methods=['GET'])
@token_required
def get_cart():
    try:
        data = request.json
        print(data)
        return 'Hola'
    except Exception as error:
        return jsonify({'error': str(error)}), 305