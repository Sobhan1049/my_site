# Generated by Django 5.1.2 on 2024-11-02 07:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("reservations", "0001_initial"),
        ("rooms", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="guest",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reservations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reservations",
                to="rooms.room",
            ),
        ),
        migrations.AddField(
            model_name="bookedday",
            name="reservation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="reservations.reservation",
            ),
        ),
    ]
