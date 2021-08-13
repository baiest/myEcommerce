from flask import (
    Blueprint
    ,jsonify
    )
from database.sql import *
from .Login import token_required

categories = Blueprint('categories', __name__, url_prefix='/categories')

@categories.route('/', methods=['GET'])
def get_categories():
    return jsonify(select('categories')), 200
