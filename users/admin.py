from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin


@admin.register(models.User)
class CustomUseradmin(UserAdmin):
    '''custom user admin '''

    fieldsets = UserAdmin.fieldsets + (("custom profile", {"fields": ('avatar', 'gender',"bio")}),)


