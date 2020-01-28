from django.db import models
from django.contrib.auth.models import User
from app.other_constants import *

#**************************************************************************
#   CONTACT'S DATA
#**************************************************************************
class Contacts(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE, db_index = True, null = True,)

    app_id = models.CharField(
        max_length = 30,
        db_index = True,
        blank = True,
        null = True,
    )

    is_imported_user = models.BooleanField(
        default = False,
        db_index = True,
        choices = user_constants.IS_TRUE,
        blank = True,
    )

    imported_user = models.OneToOneField(
        User,
        related_name = 'imported_user',
        db_index = True,
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
    )

    is_customer = models.BooleanField(
        db_index = True,
        choices = user_constants.IS_TRUE,
        default = False,
        null = True,
        blank = True,
    )

    is_vendor = models.BooleanField(
        db_index = True,
        choices = user_constants.IS_TRUE,
        default = False,
        null = True,
        blank = True,
    )

    salutation = models.IntegerField(
        db_index = True,
        default = 0,
        choices = user_constants.SALUTATIONS,
    )

    contact_name = models.CharField(
        max_length = 250,
        blank = False,
        null = False,
        db_index = True,
    )

    display_name = models.CharField(
        max_length = 250,
        blank = True,
        null = True,
        db_index = True,
    )

    organization_type = models.IntegerField(
        db_index = True,
        choices = user_constants.ORGANIZATION_TYPE,
        default = 1,
    )

    organization_name = models.CharField(
        max_length = 250,
        db_index = True,
        blank = True,
        null = True,
    )

    email = models.EmailField(
        blank = False, 
        null = False, 
        db_index = True,
    )

    website = models.CharField(
        max_length = 250,
        db_index = True,
        blank = True,
        null = True,
    )

    is_active = models.BooleanField(
        db_index = True,
        choices =  user_constants.IS_TRUE,
        default = True,
    )    

    preferred_payment_method = models.IntegerField(
        null = True,
        blank = True,
        db_index = True,
        choices = payment_constants.PREFERRED_PAYMENT_TYPE,
        default = 0
    )

    preferred_delivery = models.IntegerField(
        default = 0,
        db_index = True,
        choices = payment_constants.PREFERRED_DELIVERY,
    )

    invoice_terms = models.IntegerField(
        null = True,
        blank = True,
        db_index = True,
        choices = payment_constants.PAYMENT_DAYS,
    )

    bills_terms = models.IntegerField(
        null = True,
        blank = True,
        db_index = True,
        choices = payment_constants.PAYMENT_DAYS,
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
    
    def __str__(self):
        return self.contact_name.upper()

    def is_customer_value(self):
        if self.is_customer:
            return "YES"
        return "NO"

    def is_vendor_value(self):
        if self.is_vendor:
            return "YES"
        return "NO"

    def is_active_value(self):
        if self.is_active:
            return "YES"
        return "NO"  

    def invoice_terms_full(self):
        if self.invoice_terms is not None:
            return dict(payment_constants.PAYMENT_DAYS)[self.invoice_terms]
        return '--'
    
    def bills_terms_full(self):
        if self.bills_terms is not None:
            return dict(payment_constants.PAYMENT_DAYS)[self.bills_terms]
        return '--'

    class Meta:
        verbose_name_plural = 'contacts_tbl'


#**************************************************************************
#   EMAIL ADDRESSES OF CONTACTS
#   A CONTACT CAN HAVE MULTIPLE MAIL ADDRESSES
#**************************************************************************
class Contacts_Email(models.Model):

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
        choices = user_constants.IS_TRUE,
        default = True,
    )

    is_personal = models.BooleanField(
        db_index = True,
        choices = user_constants.IS_TRUE,
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

    def is_official_full(self):
        if self.is_official:
            return "YES"
        return "NO" 

    def is_personal_full(self):
        if self.is_personal:
            return "YES"
        return "NO" 

    class Meta:
        verbose_name_plural = 'contacts_email_tbl'


#**************************************************************************
#   ADDRESSES OF CONTACTS
#   A CONTACT CAN HAVE MULTIPLE ADDRESSES
#**************************************************************************

class Contact_Addresses(models.Model):

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

    flat_no = models.CharField(
        max_length = 250,
        blank = False,
        null = False,
        db_index = True,
    )

    street = models.CharField(
        max_length = 250,
        blank = False,
        null = False,
        db_index = True,
    )

    city = models.CharField(
        max_length = 250,
        blank = False,
        null = False,
        db_index = True,
    )

    state = models.CharField(
        max_length = 250,
        blank = False,
        null = False,
        db_index = True,
    )

    country = models.CharField(
        max_length = 5,
        null = True,
        blank = True,
        db_index = True,
        choices = country_list.COUNTRIES_LIST_CHOICES
    )

    pincode = models.CharField(
        max_length = 250,
        blank = False,
        null = False,
        db_index = True,
    )

    is_billing_address = models.BooleanField(
        db_index = True,
        choices = user_constants.IS_TRUE,
        default = False,
    ) 

    is_shipping_address = models.BooleanField(
        db_index = True,
        choices = user_constants.IS_TRUE,
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

    def is_billing_address_full(self):
        if self.is_billing_address:
            return "YES"
        return "NO"

    def is_shipping_address_full(self):
        if self.is_shipping_address:
            return "YES"
        return "NO"

    def same_billing_shipping_address_full(self):
        if self.is_billing_address == self.is_shipping_address:
            return "YES"
        return "NO"

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

    account_number = models.CharField(
        max_length = 30,
        blank = True,
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

