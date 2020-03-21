from django.db import models
from django.contrib.auth.models import User
from app.other_constants import *

from app.models import *
from django.forms import *

#
# ADDRESS FORMSET
#
AddressFormset = inlineformset_factory(contacts_model.Contacts, users_model.User_Address_Details, extra = 1,
    fields = ('contact_person', 'flat_no', 'street', 'city', 'state', 'country', 'pincode', 'is_billing_address', 'is_shipping_address'),
    widgets = {
        'contact_person' : TextInput(attrs={'class':'form-control input-sm',}),
        'flat_no' : TextInput(attrs={'class':'form-control input-sm',}),
        'street' : TextInput(attrs={'class':'form-control input-sm',}),
        'city' : TextInput(attrs={'class':'form-control input-sm',}),
        'state' : Select(attrs={'class':'form-control input-sm',}, choices = country_list.STATE_LIST_CHOICES),
        'country' : Select(attrs={'class':'form-control input-sm',}, choices = country_list.COUNTRIES_LIST_CHOICES),
        'pincode' : TextInput(attrs={'class':'form-control input-sm',}),
        'is_billing_address' : CheckboxInput(attrs={'class':'form-control input-sm',},),
        'is_shipping_address' : CheckboxInput(attrs={'class':'form-control input-sm',},),
    }
)

