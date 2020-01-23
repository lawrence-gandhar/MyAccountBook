from django.forms import *
from django.contrib.auth.models import User
from app.models.invoice_model import *
from app.models.users_model import *


#=======================================================================
#   INVOICE DESIGNER FORM
#=======================================================================

class InvoiceDesignerForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(InvoiceDesignerForm, self).__init__(*args, **kwargs)
        self.fields['billing_address'].queryset = User_Address_Details.objects.filter(user = self.user, is_billing_address = True)

    class Meta:
        IS_ACTIVE = ((True, 'YES'), (False, 'NO'))

        TEMPLATE_DESIGN = (
            (1, 'GREEN TEMPLATE'),
            (2, 'ORANGE TEMPLATE'),
            (3, 'BLUE TEMPLATE'),
            (4, 'WHITE TEMPLATE'),
            (5, 'GREY TEMPLATE'),
            (6, 'CUSTOM TEMPLATE'),
        )

        USER_NAME_ON_TEMPLATE = (
            (True, 'USE USER FIRSTNAME LASTNAME'),
            (False,'USE CUSTOM USERNAME'),
        )

        model = Invoice_Templates

        fields = (
            'template_name', 'design_number', 'logo', 'header_bgcolor', 'header_fgcolor', 
            'other_design_colors', 'is_active', 'user_display_name', 'user_custom_name',
            'user_phone', 'user_email', 'billing_address',
        )
        
        widgets = {
            'template_name' : TextInput(attrs={'class':'form-control input-sm', 'required':'true'}),
            'design_number' : Select(attrs={'class': 'form-control input-sm',}, choices = TEMPLATE_DESIGN),
            'logo' : FileInput(attrs={'class':'form-control input-sm',}),
            'header_bgcolor' : TextInput(attrs={'class':'form-control input-sm','type':'color'}),
            'header_fgcolor' : TextInput(attrs={'class':'form-control input-sm','type':'color'}),
            'other_design_colors' : TextInput(attrs={'class':'form-control input-sm','type':'color'}),
            'is_active' : Select(attrs={'class':'form-control input-sm',}, choices = IS_ACTIVE),
            'user_display_name' : Select(attrs={'class':'form-control input-sm',}, choices = USER_NAME_ON_TEMPLATE),
            'user_custom_name' : TextInput(attrs={'class':'form-control input-sm',}),
            'billing_address' : Select(attrs={'class':'form-control input-sm','required':'true'}, ),
        }


#=======================================================================
#   INVOICE FORM
#=======================================================================
class InvoiceForm(ModelForm):
    class Meta:

        model = Invoice
        fields = (
                    'service_recipient', 'recipient_billing_address', 'recipient_shipping_address',
                    'provider_billing_address', 'provider_shipping_address',
                    'provider_state_code', 'recipient_state_code', 'sac_code', 'service_description', 
                    'cgst', 'igst', 'sgst', 'total_gst', 'shipping', 'discount',
                )

        widgets = {
            'service_recipient' : Select(attrs={'class':'form-control input-sm',}),            
            'provider_state_code' : TextInput(attrs={'class':'form-control input-sm',}),
            'recipient_state_code' : TextInput(attrs={'class':'form-control input-sm',}),
            'shipping' : TextInput(attrs={'class':'form-control input-sm',}),
            'discount' : TextInput(attrs={'class':'form-control input-sm',}),
            'sac_code' : TextInput(attrs={'class':'form-control input-sm',}),
            'service_description' : TextInput(attrs={'class':'form-control input-sm',}),
            'cgst' : TextInput(attrs={'class':'form-control input-sm',}),
            'igst' : TextInput(attrs={'class':'form-control input-sm',}),
            'sgst' : TextInput(attrs={'class':'form-control input-sm',}),
            'total_gst' : TextInput(attrs={'class':'form-control input-sm',}),            
        }
        
