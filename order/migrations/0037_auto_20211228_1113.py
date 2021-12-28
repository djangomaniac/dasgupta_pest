# Generated by Django 3.0.4 on 2021-12-28 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0036_auto_20211201_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='rate_1',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='rate_2',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='rate_3',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='rate_4',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
