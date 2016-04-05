FROM python:3-onbuild

MAINTAINER Pascal Bertschi

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD *.py /

CMD [ "python", "./post.py" ]