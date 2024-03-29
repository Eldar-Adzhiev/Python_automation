#!/usr/bin/env python3.10

import os
import random

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/get_age/<name>', methods=['GET'])
def get_user_age(name):
    return jsonify(random.randint(0, 100)), 200


@app.route('/status', methods=['GET'])
def status():
    return 'OK'


if __name__ == '__main__':
    host = os.environ.get('STUB_HOST', '127.0.0.1')
    port = os.environ.get('STUB_PORT', '6000')

    app.run(host, port)
