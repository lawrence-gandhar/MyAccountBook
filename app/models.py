from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Contacts(models.Model):

    IS_ACTIVE = ((True, 'YES'), (False, 'NO'))

    contact_fname = models.CharField(
        max_leangth = 250,
        blank = False,
        null = False,
        db_index = True,
    )

    contact_lname = models.CharField(
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

    


    class Meta:
        verbose_name_plural = 'contacts_tbl'