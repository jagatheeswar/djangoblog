# Generated by Django 3.1.2 on 2021-04-12 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0009_userdetails_dropcountry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='continent',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='nickname',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='dob',
            field=models.TextField(default=0, max_length=8),
            preserve_default=False,
        ),
    ]
