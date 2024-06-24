FROM python:3.12-alpine3.20

WORKDIR .

COPY . .

CMD [ "python", "main.py" ]
