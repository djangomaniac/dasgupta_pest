# Generated by Django 3.0.4 on 2021-07-10 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0022_auto_20210710_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='invoice_for_month',
            field=models.CharField(choices=[('JANUARY', 'JANUARY'), ('FEBRUARY', 'FEBRUARY'), ('MARCH', 'MARCH'), ('APRIL', 'APRIL'), ('MAY', 'MAY'), ('JUNE', 'JUNE'), ('JULY', 'JULY'), ('AUGUST', 'AUGUST'), ('SEPTEMBER', 'SEPTEMBER'), ('OCTOBER', 'OCTOBER'), ('NOVEMBER', 'NOVEMBER'), ('DECEMBER', 'DECEMBER')], default='JAN', max_length=100),
        ),
    ]