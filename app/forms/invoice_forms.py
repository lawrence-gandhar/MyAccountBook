from django.forms import *
from app.models.invoice_model import *


#=======================================================================
#   INVOICE DESIGNER FORM
#=======================================================================

class InvoiceDesignerForm(ModelForm):

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

        model = Invoice_Templates

        fields = (
            'template_name', 'design_number', 'logo', 'header_bgcolor', 'header_fgcolor', 
            'other_design_colors', 'is_active',
        )

        widgets = {
            'template_name' : TextInput(attrs={'class':'form-control input-sm', 'required':'true'}),
            'design_number' : Select(attrs={'class': 'form-control input-sm',}, choices = TEMPLATE_DESIGN),
            'logo' : FileInput(attrs={'class':'form-control input-sm',}),
            'header_bgcolor' : TextInput(attrs={'class':'form-control input-sm','type':'color'}),
            'header_fgcolor' : TextInput(attrs={'class':'form-control input-sm','type':'color'}),
            'other_design_colors' : TextInput(attrs={'class':'form-control input-sm','type':'color'}),
            'is_active' : Select(attrs={'class':'form-control input-sm',}, choices = IS_ACTIVE),
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
                    'provider_state_code', 'recipient_state_code', 'provider_gstin', 
                    'recipient_gstin', 'provider_pan', 'sac_code', 'service_description', 'total_amount', 
                    'cgst', 'igst', 'sgst', 'total_gst', 'total_amount_after_tax'
                )

        widgets = {
            'service_recipient' : Select(attrs={'class':'form-control input-sm',}),            
            'provider_state_code' : TextInput(attrs={'class':'form-control input-sm',}),
            'recipient_state_code' : TextInput(attrs={'class':'form-control input-sm',}),
            'provider_gstin' : TextInput(attrs={'class':'form-control input-sm',}),
            'recipient_gstin' : TextInput(attrs={'class':'form-control input-sm',}),
            'provider_pan' : TextInput(attrs={'class':'form-control input-sm',}),
            'sac_code' : TextInput(attrs={'class':'form-control input-sm',}),
            'service_description' : TextInput(attrs={'class':'form-control input-sm',}),
            'total_amount' : TextInput(attrs={'class':'form-control input-sm',}),
            'cgst' : TextInput(attrs={'class':'form-control input-sm',}),
            'igst' : TextInput(attrs={'class':'form-control input-sm',}),
            'sgst' : TextInput(attrs={'class':'form-control input-sm',}),
            'total_gst' : TextInput(attrs={'class':'form-control input-sm',}),
            'total_amount_after_tax' : TextInput(attrs={'class':'form-control input-sm',}),
        }
        
