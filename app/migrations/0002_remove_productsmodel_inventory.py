# Generated by Django 2.2.3 on 2020-02-18 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsmodel',
            name='inventory',
        ),
    ]