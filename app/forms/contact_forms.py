from django.forms import *
from app.models.contacts_model import *
from app.other_constants import *

class UploadContactsForm(ModelForm):
    class Meta:
        model = ContactsFileUpload
        fields = ('csv_file',)

        widgets = {
            'csv_file' : FileInput(attrs = {'class':'form-control input-sm', 'accept': ".csv, text/csv"}),
        }

class ContactsForm(ModelForm):
    class Meta:

        model = Contacts
        fields = (
                    'customer_type', 'is_imported_user', 'imported_user', 'contact_name', 
                    'display_name', 'organization_name', 'organization_type', 'salutation',
                    'app_id', 'website', 'email', 'phone', 'facebook', 'twitter', 
                    'is_sub_customer', 'is_msme_reg', 'attachements', 'notes',
                )

        widgets = {
            'attachements' : FileInput(attrs = {'class':'form-control input-sm',}),
            'customer_type': Select(attrs={'class':'form-control input-sm'}, choices = user_constants.CUSTOMER_TYPE),
            'is_sub_customer': Select(attrs={'class':'form-control input-sm'}, choices = user_constants.IS_SUB_CUSTOMER),
            'is_msme_reg': Select(attrs={'class':'form-control input-sm'}, choices = user_constants.IS_TRUE),
            'is_imported_user': CheckboxInput(attrs={'class':'form-check-input','value':'1', 'style':'margin:5px; height:15px; width:15px;'}),
            'imported_user': TextInput(attrs={'class':'form-control input-sm', 'type':'hidden'}),
            'email': TextInput(attrs={'class':'form-control input-sm', }),
            'phone': TextInput(attrs={'class':'form-control input-sm', }),
            'website': TextInput(attrs={'class':'form-control input-sm', }),
            'salutation' : Select(attrs={'class':'form-control input-sm',}, choices = user_constants.SALUTATIONS),
            'contact_name' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'200'}),
            'display_name' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'200'}),
            'facebook' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'200'}),
            'twitter' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'200'}),
            'organization_type' : Select(attrs={'class':'form-control input-sm',}, choices = user_constants.ORGANIZATION_TYPE, ),
            'organization_name' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'200'}),
            'notes': Textarea(attrs = {'class':'form-control'})
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
        fields = ('contact_person', 'flat_no', 'street', 'city', 'state', 'country' , 'pincode', 'is_billing_address', 'is_shipping_address',)

        widgets = {
            'contact_person' : TextInput(attrs={'class':'form-control input-sm',}),
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