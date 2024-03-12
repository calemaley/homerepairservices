# Generated by Django 5.0.2 on 2024-03-10 00:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0009_booking_address_booking_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='staff',
        ),
        migrations.AddField(
            model_name='booking',
            name='ordered_by',
            field=models.CharField(default=datetime.datetime(2024, 3, 10, 0, 23, 46, 13299, tzinfo=datetime.timezone.utc), max_length=20),
            preserve_default=False,
        ),
    ]