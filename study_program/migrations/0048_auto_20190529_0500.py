# Generated by Django 2.1.2 on 2019-05-28 22:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_program', '0047_auto_20190529_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletime',
            name='appointment_date',
            field=models.DateField(default=datetime.datetime(2019, 5, 29, 5, 0, 34, 49435)),
        ),
        migrations.AlterField(
            model_name='issue',
            name='sending_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 29, 5, 0, 34, 50432)),
        ),
    ]
