FROM python:rc-alpine3.11

RUN apk update && \
    apk add --no-cache build-base

WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
