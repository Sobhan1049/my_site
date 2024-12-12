from django.contrib import admin
from . import models

@admin.register(models.Lists)
class listAdmin(admin.ModelAdmin):
    """lists admin definition"""

    list_display = ("name", "user", "count_rooms",)

    search_fields = ("name",)

    filter_horizontal = ("rooms", )