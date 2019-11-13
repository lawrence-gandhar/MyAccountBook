from django.db import models
from django.contrib.auth.models import User
from app.models.contacts_model import Contacts

class Invoice(models.Model):

    service_provider = models.ForeignKey(
        User, 
        on_delete = models.SET_NULL, 
        null = True,
        blank = True,
        db_index = True,
    )

    service_recipient = models.ForeignKey(
        Contacts, 
        on_delete = models.SET_NULL, 
        db_index = True,
        null = True,
        blank = True,
    )

    provider_state_code = models.CharField(
        max_length = 10,
        null = True,
        blank = True,
        db_index = True,
    ) 

    recipient_state_code = models.CharField(
        max_length = 10,
        null = True,
        blank = True,
        db_index = True,
    ) 

    provider_gstin = models.CharField(
        max_length = 30,
        null = True,
        blank = True,
        db_index = True,
    ) 

    recipient_gstin = models.CharField(
        max_length = 30,
        null = True,
        blank = True,
        db_index = True,
    ) 

    provider_pan = models.CharField(
        max_length = 20,
        null = True,
        blank = True,
        db_index = True,
    ) 

    sac_code = models.CharField(
        max_length = 20,
        null = True,
        blank = True,
        db_index = True,
    ) 

    service_description = models.TextField(
        blank = True,
        null = True,
    )

    total_amount = models.FloatField(
        default = 0,
        db_index = True,
    )

    cgst = models.FloatField(
        default = 0,
        db_index = True,
    )

    igst = models.FloatField(
        default = 0,
        db_index = True,
    )

    sgst = models.FloatField(
        default = 0,
        db_index = True,
    )

    total_gst = models.FloatField(
        default = 0,
        db_index = True,
    )

    total_amount_after_tax = models.FloatField(
        default = 0,
        db_index = True,
    )

    created_on = models.DateTimeField(
        auto_now = True,
        db_index = True,
    )

    class Meta:
        verbose_name_plural = 'invoice_tbl'