# chat-python
docker run:
docker run --name chat-python --rm -d -p 329:5000  -e FLASK_APP=/app/chat/app.py python-chatapp:latest flask run -h 0.0.0.0

docker-compose build:
docker-compose -f docker-compose.yml up --build

docker-compose up:
docker-compose -f docker-compose.yml up -d
