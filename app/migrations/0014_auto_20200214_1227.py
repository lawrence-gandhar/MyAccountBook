# Generated by Django 2.2.4 on 2020-02-14 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20200214_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='purchase_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchase_account', to='app.ProductAccounts'),
        ),
        migrations.AddField(
            model_name='productsmodel',
            name='sales_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_account', to='app.ProductAccounts'),
        ),
    ]