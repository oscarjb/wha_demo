# World Health Analytics (WHA) - Sentiment Analysis 

**This demo is designed to analyze the sentiment of recorded audio. Its purpose is to provide a score ranging from -1 (negative) to 1 (positive) for the audio. The intention of this demo is to be versatile and applicable in various scenarios such as restaurants, hotels, stores, etc., to gauge the perceived quality of service by clients.**

## Main Features

- Voice recording and sentiment analysis score, available on multiple devices.
- Rapid, scalable an efficient deployment using dockers.
- Adaptability to be used in other scenarios.
- Visualization and management of the audios.

## Get started

1. To run `docker-compose build`.
2. To create a superuser: `docker-compose run --rm app sh -c "python manage.py createsuperuser"`.
3. In the Django admin site, follow the steps below:
   1. Create a User.
   2. Create a Product named **sentiment_analysis** (this product can be replaced with other services in different applications).
   3. Create a Company and link the user and the previously created product.
4. Go to [http://localhost:8000](http://localhost:8000), log in, and start using the demo :).

   
    
    
    