# Generated by Django 3.1.2 on 2021-04-12 13:03

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0008_auto_20210412_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='dropcountry',
            field=django_countries.fields.CountryField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]
