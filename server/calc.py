#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json


def perform_add(prev, current):
    return prev + current


def perform_sub(prev, current):
    return prev - current


def perform_mul(prev, current):
    return prev * current


def perform_div(prev, current):
    return prev // current


def handle_eq(prev, current, action):
    if not action or not current or not action:
        return prev, current, action
    return ACTIONS[action](prev, current), None, None


def handle_op(prev, current, old_action, action):
    if not prev:
        return current, None, action
    if not current:
        return prev, current, action
    return ACTIONS[old_action](prev, current), None, action


def handle_add(prev, current, old_action):
    return handle_op(prev, current, old_action, "+")


def handle_sub(prev, current, old_action):
    return handle_op(prev, current, old_action, "-")


def handle_div(prev, current, old_action):
    return handle_op(prev, current, old_action, "/")


def handle_mul(prev, current, old_action):
    return handle_op(prev, current, old_action, "*")

# all the available actions
ACTIONS = {
    "+": perform_add,
    "/": perform_div,
    "*": perform_mul,
    "-": perform_sub,
}

# all the available inputs
INPUTS = {
    "+": handle_add,
    "/": handle_div,
    "*": handle_mul,
    "-": handle_sub,
    "=": handle_eq
}

# all the digits
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def _calculate_next_state(prev, current, old_action, input_str):
    '''
    The function receives the current state as parameters, and an input string,
    and return the new state, also as parameters.
    '''
    if input_str in INPUTS.keys():
        prev, current, old_action = INPUTS[input_str](prev, current, old_action)
    elif input_str in NUMBERS:
        if current:
            current = current * 10 + int(input_str)
        else:
            current = int(input_str)
    else:
        # error
        pass
    return prev, current, old_action


def calculate_next_state(json_state, input_str):
    '''
    The main function of the module. Receives a json state as string, and an input string,
    and return the new json state.
    '''
    if json_state and json.loads(json_state):
        state = json.loads(json_state)
        prev, current, action = _calculate_next_state(state["prev"], state["current"], state["action"], input_str)
    else:
        # first time
        if not input_str:
            return json.dumps(None)
        if input_str not in NUMBERS:
            return json.dumps(None)
        prev = None
        current = int(input_str)
        action = None
    if not current:
        if prev:
            display = prev
        else:
            display = 0
    else:
        display = current
    return json.dumps({"display": str(display), "prev": prev, "current": current, "action": action})
