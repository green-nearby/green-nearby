FROM tiangolo/uvicorn-gunicorn:python3.7

ENV MODULE_NAME="green_nearby.app"

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv \
 && pipenv install --system --deploy

COPY src/ ./
