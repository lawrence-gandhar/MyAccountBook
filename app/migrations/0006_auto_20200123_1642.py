# Generated by Django 2.2.3 on 2020-01-23 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200123_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='provider_gstin',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='provider_pan',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='recipient_gstin',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='total_amount',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='total_amount_after_tax',
        ),
    ]