# Web Calculator
Exercise for Web Development Course.
Docker compose and code for a web calculator.

## Prerequisites
```sh
git clone git@github.com:Shakedp/WebCourse.git
pip install -r requirements.txt
```

## Run from dir
```sh
python  ./server/server.py
```

## Install
```sh
python setup.py install
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
1. Make sure that the server is running with docker compose and not on its own.
1. Intall the server package (See the `Install` section).
1. Install all the requirements.

```sh
pip install -r requirements.test.txt
cd tests
py.test
```
