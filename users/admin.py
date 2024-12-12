from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin


@admin.register(models.User)
class CustomUseradmin(UserAdmin):
    '''custom user admin '''

    fieldsets = UserAdmin.fieldsets + (("custom profile", { "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",

                    )}),)

    list_filter = UserAdmin.list_filter + ("superhost",)
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active', 'language',"currency","superhost", 'is_staff', 'is_superuser',)


