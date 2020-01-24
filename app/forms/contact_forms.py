from django.forms import *
from app.models.contacts_model import *
from app.other_constants import *


class ContactsForm(ModelForm):
    class Meta:

        model = Contacts
        fields = (
                    'is_customer', 'is_vendor', 'contact_name', 
                    'organization_name', 'organization_type',
                    'business_reg_no', 'pan', 'tds', 'gstin', 'tax_reg_no',
                    'cst_reg_no', 'preferred_currency', 'opening_balance', 
                    'preferred_payment_method', 'preferred_delivery', 
                    'gst_reg_type', 'invoice_terms', 'bills_terms',
                )

        widgets = {
            'is_customer': CheckboxInput(attrs={'class':'input-sm','value':'1',}),
            'is_vendor': CheckboxInput(attrs={'class':'input-sm','value':'1',}),
            'contact_name' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'200'}),
            'organization_type' : Select(attrs={'class':'form-control input-sm',}, choices = user_constants.ORGANIZATION_TYPE, ),
            'organization_name' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'200'}),
            'business_reg_no' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'200'}),
            'pan' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'20'}),
            'tds' : NumberInput(attrs={'class':'form-control input-sm',}),
            'gst_reg_type' : Select(attrs={'class':'form-control input-sm',}, choices = user_constants.GST_REG_TYPE, ),
            'gstin' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'20'}),
            'opening_balance' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'20'}),
            'tax_reg_no' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'20'}),
            'cst_reg_no' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'20'}),
            'invoice_terms' : Select(attrs={'class':'form-control input-sm',}, choices = payment_constants.PAYMENT_DAYS, ),
            'bills_terms' : Select(attrs={'class':'form-control input-sm',}, choices = payment_constants.PAYMENT_DAYS, ),
            'preferred_currency' : Select(attrs={'class':'form-control input-sm',}, choices = payment_constants.CURRENCY, ),
            'preferred_payment_method' : Select(attrs={'class':'form-control input-sm',}, choices = payment_constants.PREFERRED_PAYMENT_TYPE, ),
            'preferred_delivery' : Select(attrs={'class':'form-control input-sm',}, choices = payment_constants.PREFERRED_DELIVERY, ),
        }

class ContactsEmailForm(ModelForm):
    class Meta:
        EMAIL_CHOICES = ((True, 'Yes'),(False, 'No'))
        
        model = Contacts_Email
        fields = ('email', 'is_official', 'is_personal')

        widgets = {
            'email' : EmailInput(attrs={'class':'form-control input-sm',}),
            'is_official' : Select(attrs={'class':'form-control input-sm',}, choices = EMAIL_CHOICES, ),
            'is_personal' : Select(attrs={'class':'form-control input-sm',}, choices = EMAIL_CHOICES, ),
        }

class ContactsAddressForm(ModelForm):
    class Meta:
        ADDRESS_CHOICES = ((True, 'Yes'),(False, 'No'))

        model = Contact_Addresses
        fields = ('contact_name', 'flat_no', 'street', 'city', 'state', 'country' , 'pincode', 'is_billing_address', 'is_shipping_address',)

        widgets = {
            'contact_name' : TextInput(attrs={'class':'form-control input-sm',}),
            'flat_no' : TextInput(attrs={'class':'form-control input-sm',}),
            'street' : TextInput(attrs={'class':'form-control input-sm',}),
            'city' : TextInput(attrs={'class':'form-control input-sm',}),
            'state' : TextInput(attrs={'class':'form-control input-sm',}),
            'country' : Select(attrs={'class':'form-control input-sm',}, choices = country_list.COUNTRIES_LIST_CHOICES),
            'pincode' : TextInput(attrs={'class':'form-control input-sm',}),
            'is_billing_address' : Select(attrs={'class':'form-control input-sm',}, choices = ADDRESS_CHOICES, ),
            'is_shipping_address' : Select(attrs={'class':'form-control input-sm',}, choices = ADDRESS_CHOICES, ),
        }

class ContactAccountDetailsForm(ModelForm):
    class Meta:
        model = Contact_Account_Details
        fields = ('account_number', 'account_holder_name', 'ifsc_code', 'bank_name', 'bank_branch_name')

        widgets = {
            'account_number' : TextInput(attrs={'class':'form-control input-sm',}),
            'account_holder_name' : TextInput(attrs={'class':'form-control input-sm',}),
            'ifsc_code' : TextInput(attrs={'class':'form-control input-sm',}),
            'bank_name' : TextInput(attrs={'class':'form-control input-sm',}),
            'bank_branch_name' : TextInput(attrs={'class':'form-control input-sm',}),
        }