server {
    
    listen ${LISTEN_PORT};

    return 301 https://nlp.whacloud.com;
}


server {

    listen ${LISTEN_PORT_SSL} ssl;    
    ssl_certificate /certs/fullchain.pem;
    ssl_certificate_key /certs/privkey.pem;



    location /static {
        alias /vol/static;
    }


    location / {
        #your proxy directives
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }

}
