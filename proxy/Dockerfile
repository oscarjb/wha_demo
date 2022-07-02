FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="wha.com"

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh