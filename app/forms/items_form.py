from django.forms import * 
from app.models.items_model import *

#===================================================================================
# PRODUCT FORM
#===================================================================================
#

class ProductForm(ModelForm):
    
    class Meta:
        model = ProductsModel

        fields = (
            'product_category', 'product_type', 'sku', 'product_name', 'product_description',
            'product_dimension', 'cost_price', 'marked_price', 'selling_price', 'discount', 
            'tax', 'gst', 'hsn_code', 'abatement', 'unit'
        )

        widgets = {
            'product_category' : Select(attrs = {'class':'form-control input-sm',})
        }