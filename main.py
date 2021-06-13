from flask import Flask, jsonify, Blueprint
from db import DataBase
from routes.Api import api


app = Flask(__name__)
app.register_blueprint(api)

@app.route('/')
def hello():
    return jsonify(data=DataBase()._query("SELECT * FROM clients"))

if __name__ == '__main__':
    app.run(debug=True)