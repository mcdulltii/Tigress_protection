FROM ubuntu:latest

RUN apt-get update && apt-get dist-upgrade -y && \
    apt-get install -y git cmake build-essential clang ca-certificates curl \
    unzip libboost-dev python3-dev python3-pip && apt-get clean

RUN pip install --upgrade pip
RUN pip install setuptools --upgrade

# Install Triton
RUN pip install triton-library

# Install Tigress_protection dependencies
RUN pip install llvmlite
RUN pip install arybo
RUN pip install lief

WORKDIR /Tigress_protection
COPY . .

ENTRYPOINT /bin/bash
