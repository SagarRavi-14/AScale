# Generated by Django 3.1.3 on 2020-12-06 11:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201206_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='time_stamp',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
