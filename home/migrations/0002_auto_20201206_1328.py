# Generated by Django 3.1.3 on 2020-12-06 07:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='time_stamp',
            field=models.DateField(default=datetime.datetime(2020, 12, 6, 7, 58, 4, 215348, tzinfo=utc)),
        ),
    ]
