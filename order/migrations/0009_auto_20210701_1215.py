# Generated by Django 3.0.4 on 2021-07-01 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20210509_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Paid(NEFT)', 'Paid(NEFT)'), ('Paid(CHEQUE)', 'Paid(CHEQUE)')], default='Pending', max_length=100),
        ),
    ]