# Generated by Django 5.1.2 on 2024-11-02 14:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reservations", "0003_alter_reservation_check_in_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="check_in",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="check_out",
            field=models.DateTimeField(),
        ),
    ]
