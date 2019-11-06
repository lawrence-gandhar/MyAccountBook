from django.db import models
from django.contrib.auth.models import User


#**************************************************************************
#   CONTACT'S DATA
#**************************************************************************
class Contacts(models.Model):

    IS_ACTIVE = ((True, 'YES'), (False, 'NO'))

    contact_name = models.CharField(
        max_length = 250,
        blank = False,
        null = False,
        db_index = True,
    )

    contact_email = models.CharField(
        max_length = 250,
        blank = True,
        null = True,
        db_index = True,
    )

    is_active = models.BooleanField(
        db_index = True,
        choices =  IS_ACTIVE,
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

    class META:
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

    is_official = models.Model(
        db_index = True,
        choices = EMAIL_CHOICES,
        default = True,
    )

    is_primary = models.Model(
        db_index = True,
        choices = EMAIL_CHOICES,
        default = True,
    )

    created_on = models.DateTimeField(
        auto_now = True,
        db_index = True,
    )

    class META:
        verbose_name_plural = 'contacts_email_tbl'
