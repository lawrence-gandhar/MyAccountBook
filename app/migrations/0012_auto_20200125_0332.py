# Generated by Django 2.2.3 on 2020-01-24 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200125_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='organization_type',
            field=models.IntegerField(choices=[(1, 'Individual'), (2, 'Proprietorship'), (3, 'LLP'), (4, 'Partnership'), (5, 'Trust'), (6, 'Gvt organisation')], db_index=True, default=1),
        ),
    ]