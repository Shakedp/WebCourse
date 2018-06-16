import json

from server import calc


def test_calc(phrase_and_expected):
    phrase, expected = phrase_and_expected
    state = None
    while phrase != '':
        state = calc.calculate_next_state(state, phrase[0])
        phrase = phrase[1:]

    assert json.loads(state)['display'] == expected
