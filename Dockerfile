FROM python:3-alpine

RUN apk add gettext

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt
COPY ./entrypoint.sh /app/entrypoint.sh
RUN pip install -r /app/requirements.txt

COPY ./demochecklist /app/demochecklist

WORKDIR /app/demochecklist

ENTRYPOINT [ "sh", "/app/entrypoint.sh" ]
