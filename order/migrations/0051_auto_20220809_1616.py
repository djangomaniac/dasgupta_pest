# Generated by Django 3.0.4 on 2022-08-09 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_service_company'),
        ('order', '0050_auto_20220809_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_details',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='remark',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='service_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_1', to='service.Service'),
        ),
        migrations.AlterField(
            model_name='order',
            name='service_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_2', to='service.Service'),
        ),
        migrations.AlterField(
            model_name='order',
            name='service_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_3', to='service.Service'),
        ),
        migrations.AlterField(
            model_name='order',
            name='service_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_4', to='service.Service'),
        ),
    ]
