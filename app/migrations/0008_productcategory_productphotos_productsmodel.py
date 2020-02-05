# Generated by Django 2.2.4 on 2020-02-05 06:51

import app.models.items_model
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200201_0721'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_parent', models.BooleanField(db_index=True, default=True)),
                ('category_name', models.CharField(db_index=True, max_length=250)),
                ('category_description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], default=True)),
                ('category_photo', models.FileField(upload_to='')),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProductCategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.IntegerField(choices=[(0, 'GOODS'), (1, 'SERVICES'), (2, 'BUNDLE')], db_index=True, default=0)),
                ('sku', models.CharField(db_index=True, max_length=20)),
                ('product_name', models.CharField(db_index=True, max_length=250)),
                ('product_description', models.TextField(blank=True, null=True)),
                ('product_dimension', models.TextField(blank=True, null=True)),
                ('cost_price', models.IntegerField(db_index=True, default=0)),
                ('marked_price', models.IntegerField(db_index=True, default=0)),
                ('selling_price', models.IntegerField(db_index=True, default=0)),
                ('discount', models.IntegerField(db_index=True, default=0)),
                ('tax', models.IntegerField(db_index=True, default=0)),
                ('gst', models.IntegerField(db_index=True, default=0)),
                ('hsn_code', models.CharField(blank=True, db_index=True, max_length=250, null=True)),
                ('abatement', models.IntegerField(db_index=True, default=0)),
                ('unit', models.IntegerField(db_index=True, default=0)),
                ('product_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.ProductCategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.FileField(blank=True, db_index=True, null=True, upload_to=app.models.items_model.product_file_rename)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ProductsModel')),
            ],
        ),
    ]
