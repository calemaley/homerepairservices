# Generated by Django 5.0.2 on 2024-02-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('specialization', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'ServiceProvider',
            },
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.CharField(max_length=70),
        ),
    ]
