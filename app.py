from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    return "test"


if __name__ == '__main__':
    app.run(debug=True)
