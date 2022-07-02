#!/bin/sh

set -e

# Basically acepts the template and it outputs the actual file which will
# contain the same template script or the same template but replaced with 
# the real values of environment variables
envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf

# start the NGINX server
nginx -g 'daemon off;'