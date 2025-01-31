FROM python:3.12.7-alpine

COPY .env /easypepe-lite/
COPY main.py /easypepe-lite/
COPY params.py /easypepe-lite/
COPY requirements.txt /easypepe-lite/
COPY utils.py /easypepe-lite/
WORKDIR /easypepe-lite/

RUN python -m pip install -U pip && \
    pip install -r requirements.txt

EXPOSE 4556
ENTRYPOINT ["python", "./main.py"]