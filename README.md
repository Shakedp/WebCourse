# Web Calculator
Exercise for Web Development Course.
Docker compose and code for a web calculator.
Uses python3 only

## Prerequisites
Project and tests:
- python3
- docker
- docker-compose
- chrome
- chromedriver for selenium

```sh
git clone git@github.com:Shakedp/WebCourse.git
pip3 install -r requirements.txt
```

## Run from dir
```sh
python3  ./server/server.py
``

## Install
```sh
python3 setup.py install
```

## Run with docker
```sh
docker build -t webcoursecalculator .
docker run -v $(pwd)/server:/server -p 3000:80 -w /server -i webcoursecalculator python3 server.py --host 0.0.0.0 --port 80
```

## Run with docker compose
```sh
docker-compose up
```

## Tests
There are three types of tests to this project - unit, integration & e2e, all written using pytest.
In order to run the tests you need to 
1. Intall the server package (See the `Install` section).
1. Install all the requirements.
1. Run the tests.

Python requirements:
```sh
pip3 install -r requirements.test.txt
```
Run the tests:
```sh
cd tests
py.test
```
