from django.forms import * 
from app.models.items_model import *
from app.other_constants import *

#===================================================================================
# PRODUCT FORM
#===================================================================================
#

class ProductForm(ModelForm):
        
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['sales_account'].queryset = ProductAccounts.objects.filter(user = self.user, is_sales = True, is_active = True,)
        self.fields['purchase_account'].queryset = ProductAccounts.objects.filter(user = self.user, is_sales = False, is_active = True,)
        self.fields['stock'].queryset = StockModel.objects.filter(user = self.user)

    class Meta:
        model = ProductsModel

        fields = (
            'product_type', 'sku', 'product_name', 'product_description', 'product_dimension', 
            'cost_price', 'marked_price', 'selling_price', 'discount', 'tax', 'gst', 'stock', 
            'hsn_code', 'abatement', 'unit', 'is_sales', 'is_purchase', 'sales_account', 'purchase_account',
        )

        widgets = {
            'stock' : Select(attrs = {'class':'form-control input-sm,'}),
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
            'unit' : Select(attrs = {'class':'form-control input-sm'}, choices = items_constant.UNITS),
            'is_sales' : CheckboxInput(attrs = {'class':'form-check-input input-sm', 'checked':'true'},),
            'is_purchase' : CheckboxInput(attrs = {'class':'form-check-input', 'checked':'true'},),
            'purchase_account' : Select(attrs = {'class':'form-control input-sm'},),
            'sales_account' : Select(attrs = {'class':'form-control input-sm'},),
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

#==================================================================================
# INVENTORY FORM
#==================================================================================
#

class InventoryForm(ModelForm):

    class Meta:
        
        model = StockModel

        fields = ('stock_name', 'in_date',)

        widgets = {
            'stock_name' : TextInput(attrs = {'class':'form-control input-sm'}),
            'in_date' : DateInput(attrs={'class':'form-control input-sm', 'type':'date', 'data-toggle':'datepicker'}),
        }


        