# Generated by Django 2.1.2 on 2019-05-30 20:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_program', '0080_auto_20190531_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletime',
            name='appointment_date',
            field=models.DateField(default=datetime.datetime(2019, 5, 31, 3, 55, 48, 444037)),
        ),
        migrations.AlterField(
            model_name='issue',
            name='sending_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 31, 3, 55, 48, 445061)),
        ),
    ]