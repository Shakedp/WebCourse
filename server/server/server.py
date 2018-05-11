#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flask
import flaskrun
import json

import calc

app = flask.Flask(__name__)


@app.route('/calculate', methods=['POST'])
def calculate():
    j = flask.request.get_json()
    print(j)
    state = j["calculatorState"]
    calc_input = j["input"]

    return calc.calculate_next_state(json.dumps(state), calc_input)

 
@app.route('/', methods=['GET'])
def main():
    return "Hello calc"


if __name__ == '__main__':
    flaskrun.flaskrun(app)
