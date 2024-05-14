from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

class Room(core_models.TimeStampedModel):

    '''room model definition'''
    name = models.CharField(max_length=40)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    guests = models.IntegerField()
    address = models.CharField(max_length=140)
    bedrooms = models.IntegerField()
    beds = models.IntegerField()
    bathrooms = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField()
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
