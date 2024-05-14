from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    '''custom user model'''

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_CHOICES = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female")

    )
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_PERSIAN = "per"
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "en"),
        (LANGUAGE_PERSIAN, "per")

    )

    CURRENCY_USD = "usd"
    CURRENCY_PER = "rial"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "usd"),
        (CURRENCY_PER, "rial")
    )

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(null=True,blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=3, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=10, blank=True)
    superhost = models.BooleanField(default=False)
