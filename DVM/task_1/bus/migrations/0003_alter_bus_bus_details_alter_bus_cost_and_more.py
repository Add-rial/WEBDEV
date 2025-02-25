# Generated by Django 5.1.5 on 2025-02-11 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0002_alter_bus_bus_details_alter_bus_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='bus_details',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='cost',
            field=models.IntegerField(default=500),
        ),
        migrations.AlterField(
            model_name='bus',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 11, 17, 20, 36, 488985), max_length=32),
        ),
        migrations.AlterField(
            model_name='bus',
            name='filled_seats',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='max_capacity',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='bus',
            name='registration_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 11, 17, 20, 36, 488985), max_length=32),
        ),
        migrations.AlterField(
            model_name='bus_stop',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
