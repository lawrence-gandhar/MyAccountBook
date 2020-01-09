from django.db import models
from django.contrib.auth.models import User
from app.models.contacts_model import Contacts
  
#=====================================================================
# MULTIPLE COLLECTION METHODS
#=====================================================================
class Collections(models.Model):

    PAYMENT_MODES = (
        (1, 'Cash'),
        (2, 'Cheque'),
        (3, 'Demand Draft'),
        (4, 'Payment Gateway'),
    )

    COLLECTION_STATUS = (
        (1, 'Collection Expected'),
        (2, 'Still Collecting'),
        (3, 'Collected'),
    )

    user = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        db_index = True,
        blank = True,
        null = True,
    )

    contact = models.ForeignKey(
        Contacts,
        on_delete = models.SET_NULL,
        db_index = True,
        blank = True,
        null = True,
    )

    collection_due_date = models.DateTimeField(
        null = True,
        blank = True,
        db_index = True,
    )

    amount = models.FloatField(
        blank = True,
        null = True,
        db_index = True,
    )

    payment_type = models.IntegerField(
        null = True,
        blank = True,
        db_index = True,
        choices = PAYMENT_MODES,
    )

    collection_status = models.IntegerField(
        null = True,
        blank = True,
        db_index = True,
        choices = COLLECTION_STATUS,
    )

    collection_date = models.DateTimeField(
        null = True,
        blank = True,
        db_index = True,
    )

    created_on = models.DateTimeField(
        db_index = True,
        auto_now_add = True,
        auto_now = False,
    )

    def __str__(self):
        return self.contact.contact_name