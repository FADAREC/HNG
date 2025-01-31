from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

EMAIL = "fadarefolajimi67@gmail.com"
GITHUB_URL = "https://github.com/FADAREC/HNG/Python_version"

@app.route('/', methods=['GET'])
def get_info():
    current_datetime = datetime.utcnow().isoformat() + "Z"

    response = {
        "email": EMAIL,
        "current_datetime": current_datetime,
        "github_url": GITHUB_URL
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
