from flask import Flask, make_response
from flask_cors import CORS
from datetime import datetime
from collections import OrderedDict
import json

app = Flask(__name__)
CORS(app)

EMAIL = "fadarefolajimi67@gmail.com"
GITHUB_URL = "https://github.com/FADAREC/HNG/Python_version"

@app.route('/', methods=['GET'])
def get_info():
    current_datetime = datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

    response_data = OrderedDict([
        ("email", EMAIL),
        ("current_datetime", current_datetime),
        ("github_url", GITHUB_URL),
    ])

    response_json = json.dumps(response_data, indent=2)
    response = make_response(response_json)
    response.headers['Content-Type'] = 'application/json'

    return response, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
