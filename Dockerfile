
FROM python:2.7

MAINTAINER yu

RUN mkdir /root/code

RUN mkdir /root/code/proj

COPY requirements.txt /root/code

WORKDIR /root/code

RUN pip install --upgrade pip && pip install -r requirements.txt

# ADD . /root/code

CMD ["/bin/bash"]