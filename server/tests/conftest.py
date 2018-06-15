import pytest


@pytest.fixture(params=[
    ('1', '1'),
    ('123', '123'),
    ('12+3', '3'),
    ('12+3=', '15'),
    ('12*3=', '36'),
    ('12/3=', '4'),
    ('13/3=', '4'),
    ('12-3=', '9'),
    ('12+3*4=', '60'),
    ('/1+2=', '3'),
    ('*1+2=', '3'),
    ('+1+2=', '3'),
    ('-1+2=', '3'),
    ('=1+2=', '3'),
    ('1+2===', '3'),
], ids=[
    'single digit',
    'multiple digits',
    'no = at end',
    '= at end',
    'multiplication',
    'division - without remainder',
    'division - with remainder',
    'subtraction',
    'no precedence',
    'action at start - division',
    'action at start - multiplication',
    'action at start - addition',
    'action at start - substraction',
    'action at start - equal',
    'many equal actions',
                   ])
def phrase_and_expected(request):
    return request.param[0], request.param[1]
