from django.contrib import admin

from app.models.contacts_model import Contacts as C, Contacts_Email, Contact_Addresses, Contact_Account_Details
from app.models.invoice_model import Invoice
# Register your models here.

@admin.register(C)
class C(admin.ModelAdmin):
    model = C

@admin.register(Contacts_Email)
class Contacts_Email(admin.ModelAdmin):
    model = Contacts_Email

@admin.register(Contact_Addresses)
class Contact_Addresses(admin.ModelAdmin):
    model = Contact_Addresses

@admin.register(Contact_Account_Details)
class Contact_Account_Details(admin.ModelAdmin):
    model = Contact_Account_Details

@admin.register(Invoice)
class Invoice(admin.ModelAdmin):
    model = Invoice

