# Generated by Django 3.1.2 on 2021-04-16 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0018_auto_20210416_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonenumbers',
            name='birthday',
        ),
    ]
