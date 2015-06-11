FROM ubuntu:14.04

RUN apt-get -q -y update
RUN DEBIAN_FRONTEND=noninteractive apt-get -q -y install \
  libevent-dev \
  python-dev \
  python-pip

RUN mkdir -p /src
ADD requirements.txt /src/
RUN pip install -r /src/requirements.txt
ADD producer.py /src/

CMD ["/usr/bin/python", "/src/producer.py"]
