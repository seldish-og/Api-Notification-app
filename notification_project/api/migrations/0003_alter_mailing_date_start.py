# Generated by Django 4.1.1 on 2022-09-15 12:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_mailing_date_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='date_start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 15, 12, 4, 15, 640437)),
        ),
    ]