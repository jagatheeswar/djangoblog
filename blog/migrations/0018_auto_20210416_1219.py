# Generated by Django 3.1.2 on 2021-04-16 06:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_post_blogimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blogimage',
            field=models.ImageField(default='default.jpg', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.localtime),
        ),
    ]