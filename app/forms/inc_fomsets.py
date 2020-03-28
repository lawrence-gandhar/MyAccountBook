from django.db import models
from django.contrib.auth.models import User
from app.other_constants import *

from app.models import *
from django.forms import *

from app.forms import *

#===================================================================================
# ADDRESS FORMSET
#===================================================================================
AddressFormset = inlineformset_factory(contacts_model.Contacts, users_model.User_Address_Details, extra = 2,
    fields = ('contact_person', 'flat_no', 'street', 'city', 'state', 'country', 'pincode','is_shipping_address'),
    widgets = {
        'contact_person' : TextInput(attrs={'class':'form-control input-sm',}),
        'flat_no' : TextInput(attrs={'class':'form-control input-sm',}),
        'street' : TextInput(attrs={'class':'form-control input-sm',}),
        'city' : TextInput(attrs={'class':'form-control input-sm',}),
        'state' : Select(attrs={'class':'form-control input-sm',}, choices = country_list.STATE_LIST_CHOICES),
        'country' : Select(attrs={'class':'form-control input-sm',}, choices = country_list.COUNTRIES_LIST_CHOICES),
        'pincode' : TextInput(attrs={'class':'form-control input-sm',}),
        'is_shipping_address' : CheckboxInput(attrs={'class':'form-control input-sm hide', 'required':'false'}),
    }
)


#===================================================================================
# ACCOUNTS FORMSET
#===================================================================================

AccountsFormset = formset_factory(contact_forms.AccountDetailsForm, extra = 1)

#===================================================================================
# PRODUCT FORMSET
#===================================================================================

ProductFormSet = inlineformset_factory(invoice_model.InvoiceModel, invoice_model.InvoiceProducts, extra = 1, 
    fields=('product', 'quantity', 'inventory'),
    widgets = {
        'product' : Select(attrs = {'class':'form-control input-sm product_dropdown_select', 'onchange':'get_product_details($(this))'},),
        'quantity' : NumberInput(attrs = {'class':'form-control input-sm', 'onchange': 'product_quantity($(this))'},),
    }    
)