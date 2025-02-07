from flask import Flask, request, jsonify
import requests
import math
import threading
from collections import OrderedDict

app = Flask(__name__)

# --- Enable CORS ---
@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

# --- Utility Functions ---
def is_prime(n):
    if n < 2:
        return False
    if n in {2, 3}:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 2:
        return False
    divisors = {1}
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.update({i, n // i})
    return sum(divisors) == n

def is_armstrong(n):
    digits = list(map(int, str(n)))
    power = len(digits)
    return sum(d ** power for d in digits) == n

def fetch_fun_fact(n, result):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json", timeout=0.5)
        result["fun_fact"] = response.json().get("text", "No fun fact available.")
    except requests.exceptions.RequestException:
        result["fun_fact"] = "Fun fact not available."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    num_param = request.args.get('number')

    # --- Validate Input ---
    if not num_param or not num_param.lstrip('-').isdigit():
        return jsonify(OrderedDict([
            ("number", num_param),
            ("error", True)
        ])), 400

    num = int(num_param)

    # --- Determine Properties ---
    properties = ["even" if num % 2 == 0 else "odd"]
    if is_armstrong(num):
        properties.insert(0, "armstrong")  # Ensure ordering in JSON

    # --- Fetch Fun Fact in Parallel ---
    result = {"fun_fact": ""}
    thread = threading.Thread(target=fetch_fun_fact, args=(num, result))
    thread.start()

    # --- Construct Ordered JSON Response ---
    response_data = OrderedDict([
        ("number", num),
        ("is_prime", is_prime(num)),
        ("is_perfect", is_perfect(num)),
        ("properties", properties),
        ("digit_sum", sum(map(int, str(num)))),
    ])

    # --- Wait for Fun Fact API (max 500ms) ---
    thread.join(timeout=0.5)
    response_data["fun_fact"] = result["fun_fact"]

    return jsonify(response_data)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
