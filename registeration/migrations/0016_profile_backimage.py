# Generated by Django 3.1.2 on 2021-04-14 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0015_auto_20210413_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='backimage',
            field=models.ImageField(default='backimg.jpg', upload_to='backimg_pics'),
        ),
    ]
