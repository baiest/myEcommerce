from flask import (
    Blueprint
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
        result = select(table='product_has_category AS pro_cat', where=f'category_id = {id}', join={'products': ['pro_cat.product_id', 'products.product_id']})
        return jsonify(result)
    except Exception as error:
        return jsonify({'error':error.message}), 400

@products.route('/<string:id>', methods=['GET'])
def get_product_by_id(id):
    try:
        result = select(table='products', where=f"product_id = '{id}'")
        return jsonify(result[0])
    except Exception:
        return jsonify({'error': str(result)}), 400

@products.route('/img/<string:id>/<int:num_img>', methods=['GET'])
def get_product_img(id, num_img):
    path = os.path.join(current_app.config['IMAGES'], 'products', id)
    try:
        img =  os.listdir(path)[num_img - 1]
        return send_from_directory(path, img)
    except Exception as error:
        return jsonify({'error':str(error)}), 400