# Generated by Django 5.1.5 on 2025-02-11 13:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0005_alter_bus_end_time_alter_bus_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 11, 18, 40, 57, 717215), max_length=32),
        ),
        migrations.AlterField(
            model_name='bus',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 11, 18, 40, 57, 717215), max_length=32),
        ),
    ]
