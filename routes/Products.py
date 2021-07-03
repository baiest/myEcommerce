from flask import (
    Blueprint
    ,jsonify
    ,send_from_directory
    ,current_app
    ,request
    )
from database.sql import *
import os.path
import datetime

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
        return jsonify({'error': str(error)}), 400

@products.route('/<string:id>', methods=['GET'])
def get_product_by_id(id):
    columns = [
        'p.product_id', 
        'product_name', 
        'product_quantity', 
        'product_price',
        'array_agg(p_i.product_image) AS images'
    ]

    join = {
        'product_image AS p_i': ['p.product_id', 'p_i.product_id']
    }
    try:
        result = select(
            table='products AS p', 
            columns=columns, join=join, 
            where=f"p.product_id = '{id}'",
            group_by='p.product_id')

        if (type(result) is Exception):
            raise Exception(result)
        return jsonify(result[0])
    except Exception as error:
        return jsonify({'error': str(error)}), 205

@products.route('/img/<string:id>', methods=['GET'])
def get_product_image(id):
    path = os.path.join(current_app.config['IMAGES'], 'products', id)
    try:
        image = os.listdir(path)[0]
        return send_from_directory(path, image)
    except Exception as error:
        return jsonify({'error':str(error, path)}), 400

@products.route('/img/<string:id>/<string:name_image>', methods=['GET'])
def get_product_name_image(id, name_image):
    path = os.path.join(current_app.config['IMAGES'], 'products', id)
    try:
        return send_from_directory(path, name_image)
    except Exception as error:
        return jsonify({'error':str(error)}), 400

@products.route('/new', methods=['GET', 'POST'])
def new_product():
    try:
        data = request.json
        if not data:
            raise Exception('No hay datos')
        product = {
            'product_id': data['product_id'],
            'product_name': data['product_name'],
            'product_quantity': data['product_quantity'],
            'product_price': data['product_price'],
        }
        result = insert('products', product)

        if (type(result) is Exception):
            raise Exception(result)
        
        for category in data['category_id']:
            result = insert('product_has_category', 
            { 
                'product_id': data['product_id'], 
                'category_id': category['category_id']
            })
            if (type(result) is Exception):
                raise Exception(result)
        
        return jsonify(result)
    except Exception as error:
        return jsonify({'error': str(error)}), 205

@products.route('/new/image/<string:id>', methods=['GET', 'POST'])
def new_image_product(id):
    try:
        file = request.files['photo']
        path= os.path.join(current_app.config['IMAGES'],'products', id)
        if not os.path.isdir(path):
            os.mkdir(path)
        file.save("/".join([path, file.filename]))

        result = insert('product_image', 
            { 
                'product_id': id, 
                'product_image': file.filename
            })
        if (type(result) is Exception):
            raise Exception(result)
        return jsonify(result)
    except Exception as error:
        print(error)
        return jsonify({'error': str(error)}), 205