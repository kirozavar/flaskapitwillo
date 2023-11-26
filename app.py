from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return "Аз обицхам моето котееее"


if __name__ == '__main__':
    app.run(debug=True)
