
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
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

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"

    LOGIN_CHOICES = ((LOGIN_EMAIL, "email"),(LOGIN_GITHUB, "github"))

    avatar = models.ImageField(upload_to="avatars" ,blank=True)
    gender = models.CharField(max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(null=True,blank=True)
    language = models.CharField(max_length=15, blank=True,)
    superhost = models.BooleanField(default=False)
    currency = models.CharField(max_length=10, blank=True,)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20,default="",blank=True)
    # login_method = models.CharField(choices=LOGIN_CHOICES, max_length=50,default=LOGIN_EMAIL)

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'pk': self.pk})

