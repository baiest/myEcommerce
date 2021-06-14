from flask import Blueprint
from . import (
    Users,
    Products,
    Categories
)

api = Blueprint('api', __name__, url_prefix='/api')

""" Registers new routes """
routes = [
    Users.users,
    Products.products,
    Categories.categories
]

for route in routes:
    api.register_blueprint(route)