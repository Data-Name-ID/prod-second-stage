FROM python:3.11.7

COPY . .

RUN pip3 install -r requirements.txt

WORKDIR /project

EXPOSE 57424

ENV SERVER_PORT=57424

CMD ["sh", "-c", "exec python3 manage.py runserver 0.0.0.0:$SERVER_PORT"]
