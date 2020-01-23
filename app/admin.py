from django.contrib import admin

from app.models.contacts_model import Contacts, Contacts_Email, Contact_Addresses, Contact_Account_Details
from app.models.invoice_model import InvoiceModel, Invoice_Templates
from app.models.users_model import Profile, User_Account_Details, User_Address_Details
from app.models.collects_model import *
# Register your models here.

@admin.register(Contacts)
class C(admin.ModelAdmin):
    model = Contacts

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    model = Profile

@admin.register(User_Account_Details)
class User_Account_Details(admin.ModelAdmin):
    model = User_Account_Details 

@admin.register(User_Address_Details)
class User_Address_Details(admin.ModelAdmin):
    model = User_Address_Details 

@admin.register(Contacts_Email)
class Contacts_Email(admin.ModelAdmin):
    model = Contacts_Email

@admin.register(Contact_Addresses)
class Contact_Addresses(admin.ModelAdmin):
    model = Contact_Addresses

@admin.register(Contact_Account_Details)
class Contact_Account_Details(admin.ModelAdmin):
    model = Contact_Account_Details

@admin.register(InvoiceModel)
class Invoice(admin.ModelAdmin):
    model = InvoiceModel

@admin.register(Collections)
class Collections(admin.ModelAdmin):
    model = Collections

@admin.register(Invoice_Templates)
class Collections(admin.ModelAdmin):
    model = Invoice_Templates

