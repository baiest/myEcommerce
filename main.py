from flask import Flask, jsonify, Blueprint, send_from_directory
from flask_cors import CORS
from routes.Api import api
import os


app = Flask(__name__, static_folder='dashboard')
CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['IMAGES'] = os.path.join(os.getcwd(), 'images')
app.register_blueprint(api)

"""# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists('client/' + '/' + path):
        return send_from_directory('client/', path)
    else:
        return send_from_directory('client/', 'index.html')

@app.route('/dashboard', defaults={'path': ''})
@app.route('/dashboard/<path:path>')
def serve_dashboard(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

"""

if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True, debug=True, host='0.0.0.0')