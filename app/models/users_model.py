from django.db import models
from django.contrib.auth.models import User
from app.other_constants import country_list
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string

#**************************************************************************
#   USER'S PROFILE DETAILS
#**************************************************************************
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_index = True,)
    
    app_id = models.CharField(
        max_length = 30,
        db_index = True,
        blank = True,
        null = True,
    )

    official_phone = models.CharField(
        max_length = 30,
        db_index = True,
        blank = True,
        null = True,
    )

    personal_phone = models.CharField(
        max_length = 30,
        db_index = True,
        blank = True,
        null = True,
    )

    alternative_phone = models.CharField(
        max_length = 30,
        db_index = True,
        blank = True,
        null = True,
    )

    official_email = models.CharField(
        max_length = 250,
        db_index = True,
        blank = True,
        null = True,
    )

    personal_email = models.CharField(
        max_length = 250,
        db_index = True,
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.user.username

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

class User_Address_Details(models.Model):

    ADDRESS_CHOICES = ((True, 'Yes'),(False, 'No'))

    user = models.ForeignKey(
        User, 
        on_delete = models.CASCADE, 
        db_index = True
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

    def __str__(self):
        return self.flat_no +", "+self.street+", "+self.city

    def complete_billing_address(self):
        return self.flat_no +", "+self.street

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
        verbose_name_plural = 'user_address_details_tbl'

#==================================================================
# Create instances on User Creation
#==================================================================
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        pro = Profile.objects.create(user=instance)
        pro.app_id = 'APK-'+get_random_string(length=10)
        pro.save()

@receiver(post_save, sender=User)
def create_user_account_details(sender, instance, created, **kwargs):
    if created:
        User_Account_Details.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_user_address_details(sender, instance, created, **kwargs):
    if created:
        User_Address_Details.objects.create(user=instance)
