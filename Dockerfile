FROM alpine:3.7
RUN echo -e http://mirrors.ustc.edu.cn/alpine/v3.7/main/ > /etc/apk/repositories

LABEL Description="This image is used to start the python Flask app." Version="1.0"
ADD . /app
WORKDIR /app

RUN apk add  --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add  --update python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    pip3 install --upgrade pip setuptools -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install --trusted-host e.pypi.python.org -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
CMD ["flask", "run"]