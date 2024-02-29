FROM python:3.11.7

COPY . .

RUN pip3 install -r requirements.txt

WORKDIR /project

ENV SERVER_PORT=57424
ENV SERVER_ADDRESS=0.0.0.0:$SERVER_PORT

EXPOSE ${SERVER_PORT}

RUN exec python3 manage.py migrate

CMD ["sh", "-c", "exec python3 manage.py runserver $SERVER_ADDRESS"]
