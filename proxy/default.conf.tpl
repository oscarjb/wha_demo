server {
    
    {* Listen on whatever port we specify *}
    listen $(LISTEN_PORT);

    {* We setup a location block to catch any urls that start with /static and it's going to
    forward to /vol/static. So we can map this volume to the same volume on our app container. So 
    all the static files and media files are shared and accesible between the proxy and the app*}
    
    location /static {
        alias /vol/static
    }

    {* Other location which will catch the non static request and will forward to the uwsgi server*}
    location / {
        {* Pass the request to the uwsgi server and connect to the APP_HOST and APP_PORT*}
        uwsgi_pass  $(APP_HOST):$(APP_PORT);
        
        {* include the uwsgi_params*}
        include /etc/nginx/uwsgi_params;
        
        {* Set the maximum size of the request*}
        client_max_body_size 10M;
    }

}