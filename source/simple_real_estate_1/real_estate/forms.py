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
        