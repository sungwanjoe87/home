# Generated by Django 4.0.4 on 2022-05-21 06:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freeboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freeboard',
            name='f_createdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 21, 15, 29, 41, 185193)),
        ),
        migrations.AlterField(
            model_name='freeboard',
            name='f_updatedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 21, 15, 29, 41, 185193)),
        ),
    ]