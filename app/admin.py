from django.contrib import admin

from app.models.contacts_model import Contacts as C
# Register your models here.

@admin.register(C)
class C(admin.ModelAdmin):
    model = C

