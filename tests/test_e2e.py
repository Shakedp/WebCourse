import time
import subprocess
import os.path

import pytest
from selenium import webdriver


DOCKER_COMPOSE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'docker-compose.yml')


@pytest.fixture(scope='module', autouse=True)
def server():
    server = None
    try:
        command_line = 'docker-compose -f {path} up'.format(path=DOCKER_COMPOSE_PATH)
        print(command_line)
        server = subprocess.Popen(command_line.split())
        time.sleep(5)  # Let the server wake up
        yield server
    finally:
        server.terminate()


@pytest.fixture(scope='module')
def browser():
    return webdriver.Chrome()


@pytest.fixture(scope='module', autouse=True)
def signup(server, browser):
    browser.get('http:localhost:3000/signup')
    for input_name in ['email', 'name', 'password']:
        input_box = browser.find_element_by_name(input_name)
        input_box.send_keys('aaa')
    input_box.submit()


def map_keys(browser):
    key_map = {}
    for digit in range(0, 10):
        key_map[str(digit)] = browser.find_element_by_class_name('digit-%d' % digit)

    key_map['+'] = browser.find_element_by_class_name('operator-plus')
    key_map['-'] = browser.find_element_by_class_name('operator-subtract')
    key_map['*'] = browser.find_element_by_class_name('operator-multiply')
    key_map['/'] = browser.find_element_by_class_name('operator-divide')
    key_map['='] = browser.find_element_by_class_name('operator-equals')

    display = browser.find_element_by_class_name('display')

    return key_map, display


def test_sanity(browser, phrase_and_expected):
    phrase, expected = phrase_and_expected
    key_map, display = map_keys(browser)

    while phrase != '':
        key_map[phrase[0]].click()
        phrase = phrase[1:]
        time.sleep(0.1)

    assert display.text == expected
    browser.refresh()
