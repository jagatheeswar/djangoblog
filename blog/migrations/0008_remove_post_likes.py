# Generated by Django 3.1.2 on 2021-04-12 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
