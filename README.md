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

## Tests
There are two types of tests to this project - unit & integration. Both written using pytest.
```sh
cd server/tests
pip install -r requirements.txt
py.test
```