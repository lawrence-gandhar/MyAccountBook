# Generated by Django 2.2.3 on 2020-03-10 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200311_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicemodel',
            name='repeat_for',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoicemodel',
            name='frequency',
            field=models.IntegerField(blank=True, choices=[(0, 'WEEKLY'), (1, 'MONTHLY'), (2, 'QUARTERLY'), (2, 'HALF-YEARLY'), (2, 'YEARLY')], null=True),
        ),
    ]
