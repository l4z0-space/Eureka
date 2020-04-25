FROM python:rc-alpine3.11

RUN apk update && \
    apk add gcc

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py migrate

EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]