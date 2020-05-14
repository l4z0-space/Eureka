FROM python:3.8.2-alpine3.11

RUN apk update && \
    apk add --no-cache build-base postgresql-dev python3-dev musl-dev

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
