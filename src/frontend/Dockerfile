FROM python:3.7 AS base

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv \
 && pipenv install --system --deploy

COPY src/ ./

FROM nginx:alpine

COPY --from=base
