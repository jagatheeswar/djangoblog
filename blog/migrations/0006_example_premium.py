# Generated by Django 3.1.2 on 2020-12-10 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_example'),
    ]

    operations = [
        migrations.AddField(
            model_name='example',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]
