from django.db import models
from django.contrib.auth.models import User
from app.other_constants import *

from uuid import uuid4
import os

#==========================================================================
#   CHANGE CATEGORY FILE NAMES
#==========================================================================
#
def category_file_rename(instance, filename):

    upload_path = 'category'
    ext = filename.split('.')[-1]
    return  os.path.join(upload_path,'{}.{}'.format(uuid4().hex, ext))


#==========================================================================
#   CHANGE PRODUCT FILE NAMES
#==========================================================================
#
def product_file_rename(instance, filename):

    upload_path = 'products'
    ext = filename.split('.')[-1]
    return  os.path.join(upload_path,'{}.{}'.format(uuid4().hex, ext))

#=========================================================================================
# PRODUCT CATEGORY MODEL
#=========================================================================================
#
class ProductCategory(models.Model):
    is_parent = models.BooleanField(
        db_index = True,
        default = True,
    )

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        db_index = True,
        blank = True,
        null = True,
    )

    parent_category = models.ForeignKey(
        'self',
        db_index = True,
        on_delete = models.CASCADE,
    )

    category_name = models.CharField(
        max_length = 250,
        db_index = True,
        null = False,
        blank = False,
    )

    category_description = models.TextField(
        blank = True,
        null = True,
    )

    is_active = models.BooleanField(
        default = True,
        choices = user_constants.IS_TRUE,
    )
    
    category_photo = models.FileField(
        upload_to = ''
    )

    def __str__(self):
        return self.category_name.upper()

#=========================================================================================
# ITEMS/PRODUCT MODEL
#=========================================================================================
#
class ProductsModel(models.Model):

    user = models.ForeignKey(
        User,
        db_index = True,
        on_delete = models.SET_NULL,
        blank = True,
        null = True,
    )

    product_category = models.ForeignKey(
        ProductCategory,
        on_delete = models.SET_NULL,
        blank = True,
        null = True,
        db_index = True,
    )

    product_type = models.IntegerField(
        db_index = True,
        default = 0,
        choices = items_constant.PRODUCT_TYPE,
    )

    sku = models.CharField(
        max_length = 20,
        db_index = True,
        null = False,
        blank = False,
    )

    product_name = models.CharField(
        db_index = True,
        blank = False,
        null = False,
        max_length = 250,
    )

    product_description = models.TextField(
        blank = True,
        null = True,
    )

    product_dimension = models.TextField(
        blank = True,
        null = True,
    )

    cost_price = models.IntegerField(
        default = 0,
        db_index = True,
    )

    marked_price = models.IntegerField(
        default = 0,
        db_index = True,
    )

    selling_price = models.IntegerField(
        db_index = True,
        default = 0,
    )

    discount = models.IntegerField(
        db_index = True,
        default = 0,
    )

    tax = models.IntegerField(
        default = 0,
        db_index = True,
    )

    gst = models.IntegerField(
        default = 0,
        db_index = True,
    )

    hsn_code = models.CharField(
        max_length = 250,
        db_index = True,
        blank = True,
        null = True,
    )

    abatement = models.IntegerField(
        default = 0,
        db_index = True,
    )

    unit = models.IntegerField(
        default = 0,
        db_index = True,
    )

    def __str__(self):
        return "{} - ({})".format(self.product_name.upper(), self.sku.upper())

#=========================================================================================
# PRODUCT PHOTOS MODEL
#=========================================================================================
#
class ProductPhotos(models.Model):
    product = models.ForeignKey(
        ProductsModel,
        db_index = True,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
    )

    product_image = models.FileField(
        upload_to = product_file_rename,
        db_index = True,
        blank = True,
        null = True,
    )
