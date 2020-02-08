from django.forms import * 
from app.models.items_model import *
from app.other_constants import *

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
            'product_category' : Select(attrs = {'class':'form-control input-sm',}),
            'product_type' : Select(attrs = {'class':'form-control input-sm',}, choices = items_constant.PRODUCT_TYPE),
            'sku' : TextInput(attrs = {'class':'form-control input-sm',}),
            'product_name' : TextInput(attrs = {'class':'form-control input-sm',}),
            'product_dimension' : TextInput(attrs = {'class':'form-control input-sm',}),
            'product_description' : Textarea(attrs = {'class':'form-control input-sm',}),
            'cost_price' : NumberInput(attrs = {'class':'form-control input-sm',}),
            'marked_price' : NumberInput(attrs = {'class':'form-control input-sm',}),
            'selling_price' : NumberInput(attrs = {'class':'form-control input-sm',}),
            'discount' : NumberInput(attrs = {'class':'form-control input-sm',}),
            'tax' : NumberInput(attrs = {'class':'form-control input-sm',}),
            'gst' : NumberInput(attrs = {'class':'form-control input-sm',}),
            'hsn_code' : TextInput(attrs = {'class':'form-control input-sm',}),
            'abatement' : NumberInput(attrs = {'class':'form-control input-sm',}),
            'unit' : NumberInput(attrs = {'class':'form-control input-sm',}),
        }

#==================================================================================
# PRODUCT IMAGE FORM
#==================================================================================
#

class ProductPhotosForm(ModelForm):

    class Meta:

        model = ProductPhotos

        fields= ('product_image',)

        widgets = {
            'product_image' : FileInput(attrs = {'class':'form-control input-sm', 'multiple' : 'true'})
        }