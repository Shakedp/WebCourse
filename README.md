# Web Course Calculator

## Tests
TODO

## Prerequisites

```
pip install -r requirements.txt
```

## Run

```
python  ./server/server/server.py
```

## Run with docker
```
docker build -t webcoursecalculator .
docker run -v $(pwd)/server:/server -p 3000:80 -w /server/server -i webcoursecalculator python3 server.py --host 0.0.0.0 --port 80
```
