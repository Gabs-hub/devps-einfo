from flask import Flask, jsonify, send_from_directory
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder='.')

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/api/apps', methods=['GET'])
def get_apps():
    apps = [
        {"name": "App 1", "category": "Productivity", "rating": 4.5, "price": 9.99},
        {"name": "App 2", "category": "Games", "rating": 4.0, "price": 0.00},
        {"name": "App 3", "category": "Education", "rating": 4.8, "price": 4.99}
    ]
    return jsonify(apps)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
