FROM python:3.8-slim 

ARG LOGGING=INFO

RUN mkdir /app/ -p

WORKDIR /app/

RUN pip install errbot && \
    pip install errbot[slack]

COPY src/. /app/

CMD errbot
