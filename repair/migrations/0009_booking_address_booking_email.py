# Generated by Django 5.0.2 on 2024-03-10 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0008_alter_booking_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='address',
            field=models.CharField(default='address', max_length=50),
        ),
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.CharField(default='email', max_length=50),
        ),
    ]
