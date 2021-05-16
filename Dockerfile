from ubuntu:20.04

RUN apt-get clean all; apt-get update ; apt-get install -y ansible; apt-get clean all
