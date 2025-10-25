# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/health")
def health():
    return jsonify("Minzo service is online!")


def start_dev():
    app.run(debug=True)
