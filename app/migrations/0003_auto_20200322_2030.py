# Generated by Django 2.2.4 on 2020-03-22 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200322_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_address_details',
            name='is_billing_address',
            field=models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], db_index=True, default=False),
        ),
    ]
