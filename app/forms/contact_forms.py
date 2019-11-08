from django.forms import *
from app.models.contacts_model import *


class ContactsForm(ModelForm):
    class Meta:

        PAYMENT_DAYS = (
            (1, 'On Due Date'),
            (2, '10 Days'),
            (3, '20 Days'),
            (4, '30 Days'),
            (5, '60 Days'),
            (6, '90 Days'),
        )

        model = Contacts
        fields = (
                    'is_customer', 'is_vendor', 'contact_name', 
                    'pan', 'tds', 'gstin', 'invoice_terms', 'bills_terms',
                )

        widgets = {
            'is_customer': CheckboxInput(attrs={'class':'form-control input-sm','value':'1',}),
            'is_vendor': CheckboxInput(attrs={'class':'form-control input-sm','value':'1',}),
            'contact_name' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'200'}),
            'pan' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'20'}),
            'tds' : NumberInput(attrs={'class':'form-control input-sm',}),
            'gstin' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'20'}),
            'invoice_terms' : Select(attrs={'class':'form-control input-sm',}, choices = PAYMENT_DAYS, ),
            'bills_terms' : Select(attrs={'class':'form-control input-sm',}, choices = PAYMENT_DAYS, ),
        }

