# Web Calculator
Exercise for Web Development Course.
Docker compose and code for a web calculator.

## Prerequisites
```sh
git clone git@github.com:Shakedp/WebCourse.git
pip install -r requirements.txt
```

## Run
```sh
python  ./server/server/server.py
```

## Run with docker
```sh
docker build -t webcoursecalculator .
docker run -v $(pwd)/server:/server -p 3000:80 -w /server/server -i webcoursecalculator python3 server.py --host 0.0.0.0 --port 80
```

## Run with docker compose
```sh
docker-compose up
```

## Tests
There are three types of tests to this project - unit, integration & e2e, all written using pytest.
Make sure that you don't have the server running already - the tests runs it by themselves.
```sh
cd server/tests
pip install -r requirements.txt
py.test
```
