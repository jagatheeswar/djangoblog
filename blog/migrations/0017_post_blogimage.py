# Generated by Django 3.1.2 on 2021-04-15 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blogimage',
            field=models.ImageField(default='default.jpg', upload_to='blog_pics'),
        ),
    ]
