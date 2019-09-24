FROM python:3.7.4

EXPOSE 8090

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python", "./server.py"]