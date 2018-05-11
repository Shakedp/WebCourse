import json

import pytest

from server import calc


@pytest.mark.parametrize('phrase,expected', [
    ('1', '1'),
    ('123', '123'),
    ('12+3', '3'),
    ('12+3=', '15'),
    ('12*3=', '36'),
    ('12/3=', '4'),
    ('13/3=', '4'),
    ('12-3=', '9'),
    ('12+3*4=', '60')
], ids=[
    'single digit',
    'multiple digits',
    'no = at end',
    '= at end',
    'multiplication',
    'division - without remainder',
    'division - with remainder',
    'subtraction',
    'no precedence'])
def test_calc(phrase, expected):
    state = None
    while phrase != '':
        state = calc.calculate_next_state(state, phrase[0])
        phrase = phrase[1:]

    assert json.loads(state)['display'] == expected
