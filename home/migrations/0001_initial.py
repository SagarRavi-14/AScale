# Generated by Django 3.1.3 on 2020-12-05 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
