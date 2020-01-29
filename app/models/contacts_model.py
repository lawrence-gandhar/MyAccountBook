from django.db import models
from django.contrib.auth.models import User
from app.other_constants import *
from django.db.models.signals import post_save
from django.dispatch import receiver

from uuid import uuid4
import os

#==========================================================================
#   CHANGE LOGO FILE NAMES
#==========================================================================
#
def file_rename(instance, filename):

    upload_path = 'contact_csv_imports'
    ext = filename.split('.')[-1]
    return  os.path.join(upload_path,'{}.{}'.format(uuid4().hex, ext))


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

    imported_user = models.ForeignKey(
        User,
        related_name = 'imported_user',
        db_index = True,
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
    )

    customer_type = models.IntegerField(
        db_index = True,
        choices = user_constants.CUSTOMER_TYPE,
        default = 1,
        null = True,
        blank = True,
    )

    is_sub_customer = models.IntegerField(
        choices = user_constants.IS_SUB_CUSTOMER,
        default = 1,
        db_index = True,
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

    is_msme_reg = models.BooleanField(
        db_index = True,
        choices = user_constants.IS_TRUE,
        default = False,
    )

    email = models.EmailField(
        blank = True, 
        null = True, 
        db_index = True,
    )

    phone = models.CharField(
        max_length = 250,
        db_index = True,
        blank = True,
        null = True,
    )

    website = models.CharField(
        max_length = 250,
        db_index = True,
        blank = True,
        null = True,
    )

    facebook = models.CharField(
        blank = True,
        null = True,
        max_length = 250,
    )

    twitter = models.CharField(
        blank = True,
        null = True,
        max_length = 250,
    )

    is_active = models.BooleanField(
        db_index = True,
        choices =  user_constants.IS_TRUE,
        default = True,
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

    def is_active_value(self):
        if self.is_active:
            return "YES"
        return "NO"  

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
        null = True, 
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

#===================================================================================
# CONTACTS FILE UPLOAD 
#===================================================================================

class ContactsFileUpload(models.Model):

    user = models.ForeignKey(
        User,
        db_index = True,
        blank = True,
        null = True,
        on_delete = models.CASCADE,
    )

    csv_file = models.FileField(
        upload_to = file_rename,
        db_index = True,
        blank = True,
        null = True,
    )

    created_date = models.DateTimeField(
        auto_now_add = True,
        auto_now = False,
        db_index = True,
    )

    class Meta:
        verbose_name_plural = 'contacts_fileupload_tbl'
    
