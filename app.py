from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return "test2"


if __name__ == '__main__':
    app.run(debug=True)
