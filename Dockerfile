FROM python:3.8.6-slim

WORKDIR /work

RUN apt-get update && apt-get install -y netcat

COPY requirements.txt /work/

# RUN pip install -r requirements.txt

COPY entrypoint.sh setup.py setup.cfg /work/

ADD /app /work/app/

ADD /test /work/test/

ENTRYPOINT ["/work/entrypoint.sh"]