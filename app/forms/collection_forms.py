from django.forms import *
from app.models.collects_model import *
from app.models.contacts_model import *
from django.contrib.auth.models import User

class CollectionsForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(CollectionsForm, self).__init__(*args, **kwargs)
        self.fields['contact'].queryset = Contacts.objects.filter(user = self.user)

    #CONTACTS = Contacts.objects.filter(user = self.instance.user)

    class Meta:

        PAYMENT_MODES = (
            (1, 'Cash'),
            (2, 'Cheque'),
            (3, 'Demand Draft'),
            (4, 'Payment Gateway'),
        )

        COLLECTION_STATUS = (
            (1, 'Collection Expected'),
            (2, 'Still Collecting'),
            (3, 'Collected'),
        )        

        model = Collection_model
        fields = (
                    'contact', 'collection_due_date', 'amount', 'payment_type',
                    'collection_status', 'collection_date',
                )

        widgets = {
            'contact' : Select(attrs={'class':'form-control input-sm'}),
            'collection_due_date' : DateInput(attrs={'class':'form-control input-sm', 'data-toggle':'datepicker'}),
            'amount' : NumberInput(attrs={'class':'form-control input-sm'}),
            'payment_type' : Select(attrs={'class':'form-control input-sm'}, choices = PAYMENT_MODES),
            'collection_status' : Select(attrs={'class':'form-control input-sm'}, choices = COLLECTION_STATUS),
            'collection_date' : DateInput(attrs={'class':'form-control input-sm','data-toggle':'datepicker'}),
        }
