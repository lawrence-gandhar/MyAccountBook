from django.db import models
from django.contrib.auth.models import User
from app.models.contacts_model import Contacts

class Invoice_Templates(models.Model):
    template_name = models.CharField(
        max_length = 250,
        db_index = True,
        null = False,
        blank = False,
    )

    template_file_path = models.CharField(
        max_length = 250,
        db_index = True,
        null = False,
        blank = False,
    ) 

class Invoice(models.Model):

    invoice_template = models.ForeignKey(
        Invoice_Templates,
        db_index = True,
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
    )

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

    recipient_billing_address = models.CharField(
        max_length = 10,
        blank = True,
        null = True,
        db_index = True,
    )

    recipient_shipping_address = models.CharField(
        max_length = 10,
        blank = True,
        null = True,
        db_index = True,
    )

    provider_billing_address = models.CharField(
        max_length = 10,
        blank = True,
        null = True,
        db_index = True,
    )

    provider_shipping_address = models.CharField(
        max_length = 10,
        blank = True,
        null = True,
        db_index = True,
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