# Generated by Django 3.1.2 on 2020-12-03 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0005_auto_20201203_2348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetailstwo',
            old_name='jaga',
            new_name='user',
        ),
    ]