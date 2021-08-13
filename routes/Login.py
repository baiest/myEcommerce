from flask import (
    Blueprint
    ,jsonify
    ,request
    )
from database.sql import *
from dotenv import dotenv_values
import jwt

_env = dotenv_values('.env')
login = Blueprint('login', __name__, url_prefix='/login')

def token_required(func): 
    def validate_token(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        
        if not token:
            return jsonify({'message': 'a valid token is missing'})
        return func(token, *args, **kwargs)
    return validate_token

@login.route('/login', methods=['GET','POST'])
def user_login():
    try:
        data = request.json
        columns = [
            'user_email',
            'user_name',
            'user_lastname',
            'user_password'
        ]
        result = select(table='users', where=f"user_email = '{data['user_email']}'", columns=columns)
        if len(result) == 0:
            raise Exception("Usuario no encontrado")
        user = result[0]
        if user['user_password'] != data['user_password']:
            raise Exception("Contraseña incorrecta")
        
        user.pop('user_password')
        encoded_jwt = jwt.encode(user, _env['TOKEN_PASS'], algorithm="HS256")
        return jsonify({'token': encoded_jwt})
    except Exception as error:
        return jsonify({'error': str(error)}), 305