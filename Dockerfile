FROM python:3.8-alpine3.16

LABEL maintainer="wha.com"

# When we are running our application we'll print any outputs directly to the console
ENV PYTHONUNBUFFERED 1 

# copy our requirements.txt to our docker image
COPY ./requirements.txt /requirements.txt
COPY ./app /app

# The working directory of new containers made out the image should be /app
WORKDIR /app
EXPOSE 8000

    
RUN python -m venv /py && \
    apk add ffmpeg && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    /py/bin/python -m textblob.download_corpora && \
    cp -R /root/nltk_data/ /py && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media/records && \
    chown -R app:app /vol && \
    chmod -R 755 /vol 

# add to our virtual environment to our system path, then whenever we run a command 
# that uses python will automatically use the python inside the virtual environment
ENV PATH="/scripts:/py/bin:$PATH"

# Swithes the user from the ROOT to the app user
USER app
