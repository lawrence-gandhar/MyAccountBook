# Generated by Django 2.2.3 on 2020-01-09 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0024_collection_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_due_date', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('amount', models.FloatField(blank=True, db_index=True, null=True)),
                ('payment_type', models.IntegerField(blank=True, choices=[(1, 'Cash'), (2, 'Cheque'), (3, 'Demand Draft'), (4, 'Payment Gateway')], db_index=True, null=True)),
                ('collection_status', models.IntegerField(blank=True, choices=[(1, 'Collection Expected'), (2, 'Still Collecting'), (3, 'Collected')], db_index=True, null=True)),
                ('collection_date', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Contacts')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Collection_model',
        ),
    ]
