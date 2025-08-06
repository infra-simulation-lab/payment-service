FROM python:3.10-alpine

WORKDIR /app
COPY main.py .

RUN pip install --no-cache-dir flask

CMD ["python", "main.py"]
