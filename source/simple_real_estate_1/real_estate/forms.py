from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Propertyform(ModelForm):
    class Meta:
        model = Property
        fields = ('name', 'street_addr', 'city',
                  'county', 'state_abrv', 'zip', 
                  'purchase_date', 'sqr_ft', 'price_per_sqqr_ft',
                 'purchase_price',  'market_price', 'num_of_units', 'notes')
class MaintencRecordForm(ModelForm):
    class Meta:
        model = MaintRecord
        fields = ('maint_record_date', 'property', 'unit', 'notes')
class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ('property', 'name', 'unit_number', 'sqr_ft', 'price_per_sqqr_ft', 'notes')

class TenatForm(ModelForm):
    class Meta:
        model = Tenant
        fields = ('name', 'phone', 'email', 'notes')

class RentalAgreementForm(ModelForm):
    class Meta:
        model = RentalAgreement
        fields = ('unit', 'tenant', 'contract_num', 'contract_docs', 'start_date', 'end_date', 'curr_rent', 'accepted', 'active', 'payment_sched', 'notes', 'next_increase', 'last_increase')
