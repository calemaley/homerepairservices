# Generated by Django 5.0.2 on 2024-02-23 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0004_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('good', 'good'), ('bad', 'bad')], max_length=20)),
                ('brief_description', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
