# Generated by Django 4.2.4 on 2023-09-27 19:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='title',
            field=models.CharField(default=datetime.date.today, max_length=100),
            preserve_default=False,
        ),
    ]
