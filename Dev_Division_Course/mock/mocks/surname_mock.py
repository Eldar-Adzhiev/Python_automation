#!/usr/bin/env python3.10
import os
import threading

from flask import Flask, jsonify, request

import settings

app = Flask(__name__)

SURNAME_DATA = {}


@app.route('/get_surname/<name>', methods=['GET'])
def get_user_surname(name):
    if surname := SURNAME_DATA.get(name):
        return jsonify(surname), 200
    else:
        return jsonify(f'Surname for user "{name}" not found'), 404


@app.route('/get_surname/<name>', methods=['POST'])
def post_user_surname(name):
    SURNAME_DATA[name] = request.data
    return 'OK'


@app.route('/status', methods=['GET'])
def status():
    return 'OK'


def run_mock():
    server = threading.Thread(target=app.run, kwargs={'host': settings.MOCK_HOST, 'port': settings.MOCK_PORT})
    server.start()
    return server


# deprecated, so we need to run it in subprocess
def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'Ok, exiting'), 200


# if __name__ == '__main__':
#     host = os.environ.get('MOCK_HOST', '127.0.0.1')
#     port = os.environ.get('MOCK_PORT', '7000')
#
#     app.run(host, port)
