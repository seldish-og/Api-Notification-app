# Generated by Django 4.1.1 on 2022-09-17 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_mailing_date_start'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]