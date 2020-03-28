from django.db import models
from django.contrib.auth.models import User
from app.other_constants import *

from app.models import *
from django.forms import *

#===================================================================================
# ADDRESS FORMSET
#===================================================================================
AddressFormset = inlineformset_factory(contacts_model.Contacts, users_model.User_Address_Details, extra = 2,
    fields = ('contact_person', 'flat_no', 'street', 'city', 'state', 'country', 'pincode', 'is_billing_address_diff', 'is_shipping_address'),
    widgets = {
        'contact_person' : TextInput(attrs={'class':'form-control input-sm',}),
        'flat_no' : TextInput(attrs={'class':'form-control input-sm',}),
        'street' : TextInput(attrs={'class':'form-control input-sm',}),
        'city' : TextInput(attrs={'class':'form-control input-sm',}),
        'state' : Select(attrs={'class':'form-control input-sm',}, choices = country_list.STATE_LIST_CHOICES),
        'country' : Select(attrs={'class':'form-control input-sm',}, choices = country_list.COUNTRIES_LIST_CHOICES),
        'pincode' : TextInput(attrs={'class':'form-control input-sm',}),
        'is_billing_address_diff' : CheckboxInput(attrs={'class':'form-control input-sm', 'onclick':'billing_clicked($(this))',}),
        'is_shipping_address' : CheckboxInput(attrs={'class':'form-control input-sm',}),
    }
)


#===================================================================================
# ACCOUNTS FORMSET
#===================================================================================

class AccountDetailsForm(ModelForm):
    class Meta:
        model = users_model.User_Account_Details
        fields = ('account_number', 'account_holder_name', 'ifsc_code', 'bank_name', 'bank_branch_name')

        widgets = {
            'account_number' : NumberInput(attrs={'class':'form-control input-sm', 'pattern':'[0-9]'}),
            'account_holder_name' : TextInput(attrs={'class':'form-control input-sm',}),
            'ifsc_code' : TextInput(attrs={'class':'form-control input-sm', 'onkeyup':'valid_IFSC($(this))', 'onfocusout':'valid_IFSC($(this))'}),
            'bank_name' : TextInput(attrs={'class':'form-control input-sm',}),
            'bank_branch_name' : TextInput(attrs={'class':'form-control input-sm',}),
        }

AccountsFormset = formset_factory(AccountDetailsForm, extra = 1)

#===================================================================================
# BUNDEL-PRODUCT FORMSET
#===================================================================================

