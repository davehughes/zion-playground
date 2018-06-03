ARG VERSION=latest
FROM zionlang:${VERSION}

WORKDIR /opt/zion-playground
ADD . /opt/zion-playground

ENV ZION_PATH /opt/zion
ENV FLASK_APP zion_playground/app.py
ENV FLASK_DEBUG 0
ENV FLASK_PORT 5000
ENV FLASK_HOST 0.0.0.0
CMD make serve
