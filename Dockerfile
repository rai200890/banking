FROM python:3.6.3
WORKDIR /code
RUN apt-get -qq update && apt-get install -y git ca-certificates libpq-dev
RUN pip3 install --upgrade pip
ADD requirements.txt requirements-dev.txt /code/
RUN pip3 install -r requirements-dev.txt
