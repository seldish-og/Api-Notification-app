# Generated by Django 4.1.1 on 2022-09-15 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_mailing_date_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='date_start',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
