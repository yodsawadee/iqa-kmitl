# Generated by Django 2.1.2 on 2019-05-29 20:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_program', '0074_auto_20190530_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletime',
            name='appointment_date',
            field=models.DateField(default=datetime.datetime(2019, 5, 30, 3, 15, 1, 916211)),
        ),
        migrations.AlterField(
            model_name='issue',
            name='sending_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 30, 3, 15, 1, 917186)),
        ),
    ]