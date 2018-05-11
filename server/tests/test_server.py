import json
import subprocess
import os
import time

import pytest
import requests

SERVER_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'server', 'server.py')
PORT = 9000


@pytest.fixture(scope='session', autouse=True)
def run_server():
    server = None
    try:
        command_line = 'python3 {server_path} --port {port}'.format(server_path=SERVER_PATH, port=PORT)
        server = subprocess.Popen(command_line.split())
        time.sleep(1) # Let the server wake up
        yield
    finally:
        server.terminate()


def server_calc(state, char):
    print({"calculatorState": state, "input": char})
    response = requests.post('http://localhost:9000/calculate',
                             headers={'content-type': 'application/json'},
                             data=json.dumps({"calculatorState": state, "input": char}))
    return response.content.decode()


def test_server(phrase_and_expected):
    phrase, expected = phrase_and_expected

    state = None
    while phrase != '':
        state = json.loads(server_calc(state, phrase[0]))
        phrase = phrase[1:]

    assert state['display'] == expected
