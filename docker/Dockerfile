ARG VERSION=latest
FROM zionlang/zion:${VERSION}

WORKDIR /opt/zion-playground
ADD . /opt/zion-playground

RUN apt install -y python-virtualenv
RUN rm -rf env/ && \
    virtualenv env && \
    env/bin/pip install -U pip && \
    env/bin/pip install -r requirements.txt

ENV ZION_PATH /opt/zion
ENV FLASK_APP zion_playground/app.py
ENV FLASK_DEBUG 0
ENV FLASK_PORT 5000
ENV FLASK_HOST 0.0.0.0
CMD make serve
