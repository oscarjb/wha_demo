FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="wha.com"

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh
COPY /etc/letsencrypt/live/whacloud.com/fullchain.pem /certs/fullchain.pem
COPY /etc/letsencrypt/live/whacloud.com/privkey.pem /certs/privkey.pem

ENV LISTEN_PORT=8000
ENV LISTEN_PORT_SSL=443
ENV APP_HOST=app
ENV APP_PORT=9000

USER root

RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /run.sh && \
    chown nginx:nginx /certs/fullchain.pem && \
    chown nginx:nginx /certs/privkey.pem && \
    chmod +x /run.sh

VOLUME /vol/static

USER nginx

CMD ["/run.sh"]