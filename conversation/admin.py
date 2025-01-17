from django.contrib import admin
from . import models

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """message admin definition"""


    list_display = ("__str__", "created")


@admin.register(models.conversation)
class ConversationAdmin(admin.ModelAdmin):
    """message admin definition"""


    list_display = ("__str__", "count_messages", "count_participants")