FROM python:3.11-slim-buster

COPY requirements.txt /

RUN pip install -r requirements.txt

COPY main.py /main.py
COPY app /app

WORKDIR app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]