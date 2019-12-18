from django.db import models
from django.contrib.auth.models import User
from app.other_constants import country_list

#**************************************************************************
#   USER'S PROFILE DETAILS
#**************************************************************************
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_index = True,)

    class Meta:
        verbose_name_plural = 'user_profile_tbl'

#**************************************************************************
#   USER'S ACCOUNT DETAILS
#**************************************************************************
class User_Account_Details(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        db_index = True,
    )

    account_number = models.CharField(
        max_length = 30,
        null = True,
        blank = True,
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
        verbose_name_plural = 'user_account_details_tbl'


#**************************************************************************
#   ADDRESSES OF CONTACTS
#   A CONTACT CAN HAVE MULTIPLE ADDRESSES
#**************************************************************************

class User_Addresses(models.Model):

    ADDRESS_CHOICES = ((True, 'Yes'),(False, 'No'))

    contact = models.ForeignKey(
        User, 
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
