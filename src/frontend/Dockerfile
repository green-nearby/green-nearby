FROM python:3.7 AS base

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install \
    gunicorn[gthread] \
    pipenv \
 && pipenv install --system --deploy

COPY ./ ./

CMD ["gunicorn", "--worker-tmp-dir=/dev/shm", "--bind=0.0.0.0", "--workers=2", "--threads=4", "--worker-class=gthread", "--log-file=-", "app:server"]
