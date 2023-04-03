# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY device.py device.py
COPY redisCon.py redisCon.py


#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


CMD [ "python", "redisCon.py"]