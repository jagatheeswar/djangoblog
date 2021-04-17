# Generated by Django 3.1.2 on 2021-04-13 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0013_phonenumbers_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='dob',
        ),
        migrations.AddField(
            model_name='phonenumbers',
            name='date',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phonenumbers',
            name='month',
            field=models.CharField(default=0, max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phonenumbers',
            name='year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]