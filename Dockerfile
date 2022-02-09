FROM python:3.6.13-slim
MAINTAINER Sahil Shah

# Install dependencies
RUN apt-get update \
    && pip install --upgrade pip

WORKDIR /steel-defect-detection

COPY ./requirements.txt /steel-defect-detection/requirements.txt

RUN pip install --no-cache-dir -q -r /steel-defect-detection/requirements.txt

COPY ./ /steel-defect-detection/

CMD uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000} --reload --debug













