from flask import Flask, jsonify, Blueprint
from flask_cors import CORS
from routes.Api import api


app = Flask(__name__)
CORS(app)
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)