# FROM centos:latest
FROM python:3.6.8-alpine3.9

LABEL MAINTAINER="Igor Gonçalves <igor_goncalves@live.com>"

RUN apk add build-base

COPY . /srv/nutridata/

# RUN curl -sL https://dl.yarnpkg.com/rpm/yarn.repo -o /etc/yum.repos.d/yarn.repo

# RUN dnf -y install python3 python3-pip nodejs yarn

# WORKDIR /srv/nutridata/client/

# RUN yarn && yarn build

WORKDIR /srv/nutridata/server/

RUN pip install -r requirements.txt

EXPOSE 4000

CMD ["gunicorn"  , "-b", "0.0.0.0:4000", "app:app"]