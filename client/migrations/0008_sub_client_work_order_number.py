# Generated by Django 3.0.4 on 2022-08-09 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_remove_sub_client_challan_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_client',
            name='work_order_number',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
