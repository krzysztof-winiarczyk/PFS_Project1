FROM python:alpine
WORKDIR /usr/src/app
COPY main.py main.py
CMD [ "python", "./main.py" ]