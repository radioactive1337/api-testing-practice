FROM python:3.12.0-alpine3.18
#ARG run_env
#ENV env $run_env
LABEL tests="api"
WORKDIR .
VOLUME /allure-results
RUN apk update && apk upgrade
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD pytest test --alluredir=allure-results