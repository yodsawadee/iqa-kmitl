# Generated by Django 2.1.2 on 2019-05-28 21:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_program', '0046_auto_20190529_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletime',
            name='appointment_date',
            field=models.DateField(default=datetime.datetime(2019, 5, 29, 4, 59, 40, 20644)),
        ),
        migrations.AlterField(
            model_name='issue',
            name='sending_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 29, 4, 59, 40, 21642)),
        ),
    ]
