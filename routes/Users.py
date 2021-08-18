from flask import Blueprint, request, jsonify
from database.sql import *
from dotenv import dotenv_values
from database.sql import *
from .Login import token_required
import jwt

_env = dotenv_values('.env')
users = Blueprint('users', __name__, url_prefix='/users')

def decode_token(token):
    return jwt.decode(token, _env['TOKEN_PASS'], algorithms=["HS256"])

@users.route('/', methods=['GET'])
def get_users():
    return jsonify(select('users'))

@users.route('/auth', methods=['POST'])
def auth():
    try:
        token = request.headers['token']
        result = decode_token(token)
        cart = select(table='client_cart', columns=['COUNT(*)'], where= f"client_id = '{result['user_email']}'")
        if (type(result) is Exception):
            raise Exception(cart)
        result['cart'] = cart[0]['count']
        return jsonify(result)
    except jwt.exceptions.InvalidSignatureError as error:
        return jsonify({'error': 'Token invalido'}), 305
    except Exception as error:
        print(error)
        return jsonify({'error': str(error)}), 305
    
@users.route('/cart', methods=['GET'])
#@token_required
def get_cart():
    try:
        token = request.headers['token']
        user_email = decode_token(token)['user_email']
        columns = [
            'cart.product_id', 
            'product_name', 
            'cart.quantity', 
            'product_price',
        ]
        result = select(
        table='client_cart AS cart',
        where= f"cart.client_id = '{user_email}'",
        join={'products': ['cart.product_id', 'products.product_id']},
        columns=columns)
        if (type(result) is Exception):
                raise Exception(result)
        return jsonify(result)
    except Exception as error:
        return jsonify({'error': str(error)}), 305