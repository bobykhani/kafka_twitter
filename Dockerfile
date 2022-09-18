FROM ubuntu:latest

run apt update
run apt install python3 -y
RUN apt-get -y install python3-pip


WORKDIR ./usr/app/src

COPY ./scripts/producer.py ./
COPY ./scripts/consumer.py ./

COPY ./requirements.txt ./

Run pip install -r ./requirements.txt
