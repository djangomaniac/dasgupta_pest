# Generated by Django 3.0.4 on 2022-08-09 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0051_auto_20220809_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.CharField(default=datetime.datetime.now, max_length=20, null=True),
        ),
    ]
