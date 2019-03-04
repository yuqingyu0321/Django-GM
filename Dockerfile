
FROM python:2.7

COPY requirements.txt /root/django/

WORKDIR /root/django/

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["/bin/bash"]