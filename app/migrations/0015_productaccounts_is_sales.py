# Generated by Django 2.2.4 on 2020-02-14 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20200214_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='productaccounts',
            name='is_sales',
            field=models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], db_index=True, default=True),
        ),
    ]