FROM python:3.6

RUN apt-get update && apt-get install -y net-tools
RUN mkdir /home/flask_app
WORKDIR /home/flask_app
ADD ./flask_app /home/flask_app
ADD requirements.txt /home/flask_app
RUN pip3 install -r requirements.txt
ENV PORT 8000
CMD ["gunicorn", "hello:app"]