from importlib.resources import path
from itertools import product
from pyexpat import model
from django.db import models
from django_countries.fields import CountryField
from django.utils.timezone import now
from django.conf import settings
from django.urls.base import reverse

import uuid


# Create your models here.


class Products(models.Model):
    name_product = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    def __str__(self):
        return "Product: %s" % (self.name_product)

class Company(models.Model):
    name_company = models.CharField(max_length=30)
    email = models.EmailField()
    telephone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, blank=True)
    country = CountryField()
    date = models.DateTimeField(default=now, editable=False)
    product = models.ManyToManyField(Products)
    user_company = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return "Company: %s" % (self.name_company)

class Audios(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    audio_path = models.FileField(upload_to='records')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user_company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    audio_text = models.TextField(default=" ")
    score_text = models.FloatField(default = -5)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("record_detail", kwargs={"id": str(self.id)})
    