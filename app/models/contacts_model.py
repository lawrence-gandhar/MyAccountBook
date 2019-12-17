from django.db import models
from django.contrib.auth.models import User
from app.other_constants import country_list

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

    user = models.ForeignKey(User, on_delete = models.CASCADE, db_index = True, null = True,)

    is_customer = models.BooleanField(
        db_index = True,
        choices = IS_ACTIVE,
        default = False,
        null = True,
        blank = True,
    )

    is_vendor = models.BooleanField(
        db_index = True,
        choices = IS_ACTIVE,
        default = False,
        null = True,
        blank = True,
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
            return dict(self.PAYMENT_DAYS)[self.invoice_terms]
        return '--'
    
    def bills_terms_full(self):
        if self.bills_terms is not None:
            return dict(self.PAYMENT_DAYS)[self.bills_terms]
        return '--'

    def pan_value(self):
        if self.pan is not None:
            return self.pan.upper()
        return "--"

    def gstin_value(self):
        if self.gstin is not None:
            return self.gstin.upper()
        return "--"

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
        choices = ADDRESS_CHOICES,
        default = False,
    ) 

    is_shipping_address = models.BooleanField(
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

