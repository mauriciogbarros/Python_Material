# Generated by Django 2.1 on 2022-06-01 15:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 1, 15, 25, 56, 481805, tzinfo=utc)),
        ),
    ]
