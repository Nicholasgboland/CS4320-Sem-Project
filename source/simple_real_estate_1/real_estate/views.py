from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'test.html')
def properties(request):
    properties = Property.objects.all()
    return render(request, 'properties_list.html', {'properties':properties})

def createProperty(request):
    if request.method == 'POST':
        form = Propertyform(request.POST)
        if form.is_valid():
            property = form.save(commit=False)  
            
            property.save()  
            return redirect('properties_list')
    else:
        form = Propertyform()  
    
    context = {'form': form}
    return render(request, 'create_property.html', context)

def updateProperty(request, pk):
    property = Property.objects.get(pk=pk)
    if request.method == 'POST':
        form = Propertyform(request.POST, instance=property)
        if form.is_valid():
            property = form.save(commit=False)  
            property.save()  
            return redirect('properties_list')
    else:
        form = Propertyform(instance=property)  
    context = {'form': form}
    return render(request, 'create_property.html', context)

def delete_property(request, pk):
   property = Property.objects.get(pk=pk)
   if request.method == 'POST':
      try:
         print("got id")
         
         
         property.delete()
         return redirect('properties_list')
      except Property.DoesNotExist:
            # Handle the case where the project does not exist
        print("does not exist")
        return redirect('properties_list')  # Redirect to an appropriate page
   return render(request, 'delete_property.html', {'property':property})


def units(request, pk):
    units = Unit.objects.all().filter(property_id =pk)
    return render(request, 'unit_list.html', {'units':units})

def createUnit(request):
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)  
            
            unit.save()  
            return redirect('properties_list')
    else:
        form = UnitForm()  
    
    context = {'form': form}
    return render(request, 'create_unit.html', context)



def tenant(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenant_list.html', {'tenants':tenants})

def createTenant(request):
    if request.method == 'POST':
        form = TenatForm(request.POST)
        if form.is_valid():
            tenant = form.save(commit=False)  
            
            tenant.save()  
            return redirect('tenant_list')
    else:
        form = TenatForm()  
    
    context = {'form': form}
    return render(request, 'create_tenant.html', context)


def rentalAgreement(request, pk):
    rent = RentalAgreement.objects.all().filter(unit_id =pk)
    return render(request, 'rental_aggrement.html', {'rent':rent, 'pk':pk})

def createRentalAgreement(request, pk):
    if request.method == 'POST':
        form = RentalAgreementForm(request.POST)
        if form.is_valid():
            rent = form.save(commit=False)  
            
            rent.save()  
            return redirect('rental_agreement_list', pk=pk)
            #return redirect('properties_list')

    else:
        form = RentalAgreementForm()  
    
    context = {'form': form}
    return render(request, 'create_rental_agreement.html', context)

def maintence_record(request, pk):
    #property = Property.objects.get(property_id = pk)
    records = MaintRecord.objects.all().filter(property_id =pk)

    return render(request, 'maintence_record.html', {'records':records, 'pk': pk})

def createMaintenceRecord(request, pk):
    if request.method == 'POST':
        form = MaintencRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)  
            
            record.save()  
            return redirect('maintence_records', pk=pk)
    else:
        form = MaintencRecordForm()  
    
    context = {'form': form}
    return render(request, 'create_maintence_record.html', context)

