from flask import (
    Blueprint
    ,Response
    ,jsonify
    ,send_from_directory
    ,current_app
    )
from database.sql import *
import os.path

products = Blueprint('products', __name__, url_prefix='/products')

@products.route('/', methods=['GET'])
def get_products():
    return jsonify(select(table='products'))

@products.route('/category/<int:id>', methods=['GET'])
def get_products_category(id):
    try:
        result = select(table='products', where=f'product_category = {id}')
        return jsonify(result)
    except Exception as e:
        return Response(status='404')

@products.route('/img/<string:id>/<int:num_img>', methods=['GET'])
def get_product_img(id, num_img):
    path = os.path.join(current_app.config['IMAGES'], 'products', id)
    try:
        img =  os.listdir(path)[num_img - 1]
        return send_from_directory(path, img)
    except:
        return Response(status='404')