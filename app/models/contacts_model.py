from django.db import models
from django.contrib.auth.models import User


#**************************************************************************
#   CONTACT'S DATA
#**************************************************************************
class Contacts(models.Model):

    IS_ACTIVE = ((True, 'YES'), (False, 'NO'))

    PAYMENT_DAYS = (
        (1, 'On Due Date'),
        (2, '10 Days'),
        (3, '20 Days'),
        (4, '30 Days'),
        (5, '60 Days'),
        (6, '90 Days'),
    )

    is_customer = models.BooleanField(
        db_index = True,
        choices = IS_ACTIVE,
        default = False,
    )

    is_vendor = models.BooleanField(
        db_index = True,
        choices = IS_ACTIVE,
        default = False,
    )

    contact_name = models.CharField(
        max_length = 250,
        blank = False,
        null = False,
        db_index = True,
    )

    is_active = models.BooleanField(
        db_index = True,
        choices =  IS_ACTIVE,
        default = True,
    )

    pan = models.CharField(
        max_length = 10,
        db_index = True,
        null = True,
        blank = True,
    )

    gstin = models.CharField(
        max_length = 100,
        db_index = True,
        null = True,
        blank = True,
    )

    tds = models.DecimalField(
        db_index = True,
        null = True,
        blank = True,
        max_digits = 20, 
        decimal_places = 2
    )

    invoice_terms = models.IntegerField(
        null = True,
        blank = True,
        db_index = True,
        choices = PAYMENT_DAYS,
    )

    bills_terms = models.IntegerField(
        null = True,
        blank = True,
        db_index = True,
        choices = PAYMENT_DAYS,
    )

    notes = models.TextField(
        blank = True,
        null = True,
    )
    
    created_on = models.DateTimeField(
        auto_now = True,
        db_index = True,
    ) 

    updated_on = models.DateTimeField(
        auto_now = False,
        db_index = True,
        null = True,
    )

    class Meta:
        verbose_name_plural = 'contacts_tbl'


#**************************************************************************
#   EMAIL ADDRESSES OF CONTACTS
#   A CONTACT CAN HAVE MULTIPLE MAIL ADDRESSES
#**************************************************************************
class Contacts_Email(models.Model):

    EMAIL_CHOICES = ((True, 'Yes'),(False, 'No'))

    contact = models.ForeignKey(
        Contacts, 
        on_delete = models.CASCADE, 
        db_index = True
    )
    
    email = models.EmailField(
        blank = False, 
        null = False, 
        db_index = True,
    )

    is_official = models.BooleanField(
        db_index = True,
        choices = EMAIL_CHOICES,
        default = True,
    )

    is_personal = models.BooleanField(
        db_index = True,
        choices = EMAIL_CHOICES,
        default = True,
    )

    created_on = models.DateTimeField(
        auto_now = True,
        db_index = True,
    )

    updated_on = models.DateTimeField(
        auto_now = False,
        db_index = True,
        null = True,
    )

    class Meta:
        verbose_name_plural = 'contacts_email_tbl'


#**************************************************************************
#   ADDRESSES OF CONTACTS
#   A CONTACT CAN HAVE MULTIPLE ADDRESSES
#**************************************************************************

class Contact_Addresses(models.Model):

    ADDRESS_CHOICES = ((True, 'Yes'),(False, 'No'))

    contact = models.ForeignKey(
        Contacts, 
        on_delete = models.CASCADE, 
        db_index = True
    )

    contact_name = models.CharField(
        max_length = 250,
        blank = False,
        null = False,
        db_index = True,
    )

    is_billing_address = models.BooleanField(
        db_index = True,
        choices = ADDRESS_CHOICES,
        default = False,
    ) 

    is_shipping_address = models.BooleanField(
        db_index = True,
        choices = ADDRESS_CHOICES,
        default = False,
    )

    same_billing_shipping_address = models.BooleanField(
        db_index = True,
        choices = ADDRESS_CHOICES,
        default = False,
    )

    created_on = models.DateTimeField(
        auto_now = True,
        db_index = True,
    )

    updated_on = models.DateTimeField(
        auto_now = False,
        db_index = True,
        null = True,
    )

    class Meta:
        verbose_name_plural = 'contacts_address_details_tbl'


#**************************************************************************
#   CONTACT'S ACCOUNT DETAILS
#**************************************************************************

class Contact_Account_Details(models.Model):
    contact = models.ForeignKey(
        Contacts, 
        on_delete = models.CASCADE, 
        db_index = True
    )

    account_number = models.BigIntegerField(
        null = True,
        db_index = True,
    )

    account_holder_name = models.CharField(
        max_length = 250,
        blank = True,
        null = True,
        db_index = True,
    )

    ifsc_code = models.CharField(
        max_length = 20,
        null = True,
        blank = True,
        db_index = True,
    )

    bank_name = models.CharField(
        max_length = 250,
        db_index = True,
        null = True,
        blank = True,
    )

    bank_branch_name = models.CharField(
        max_length = 250,
        db_index = True,
        null = True,
        blank = True,
    )

    created_on = models.DateTimeField(
        auto_now = True,
        db_index = True,
    )

    updated_on = models.DateTimeField(
        auto_now = False,
        db_index = True,
        null = True,
    )

    class Meta:
        verbose_name_plural = 'contacts_account_details_tbl'

