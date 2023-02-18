FROM python
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD uvicorn src.green_nearby.app:app --host 0.0.0.0 --port 8000
