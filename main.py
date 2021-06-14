from flask import Flask, jsonify, Blueprint
from flask_cors import CORS
from routes.Api import api
import os


app = Flask(__name__)
CORS(app)

app.config['IMAGES'] = os.path.join(os.getcwd(), 'images')
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')