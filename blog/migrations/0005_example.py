# Generated by Django 3.1.2 on 2020-12-09 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_feedback_date_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('user', models.TextField(max_length=444)),
            ],
        ),
    ]
