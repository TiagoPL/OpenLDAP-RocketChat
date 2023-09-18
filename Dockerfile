FROM python:slim-bullseye

COPY . /app/password-expiration-check
WORKDIR /app/password-expiration-check

RUN pip install gunicorn==20.1.0 -r requirements.txt

EXPOSE 5000

CMD gunicorn --keep-alive 600 --timeout 600 -w 4 -b 0.0.0.0:5000 app:app
