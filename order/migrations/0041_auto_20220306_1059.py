# Generated by Django 3.0.4 on 2022-03-06 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0040_auto_20220306_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='area_1',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='area_2',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='area_3',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='area_4',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=10),
        ),
    ]
