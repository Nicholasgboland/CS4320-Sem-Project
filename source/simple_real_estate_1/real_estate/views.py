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


def maintence_record(request):
    records = MaintRecord.objects.all()
    return render(request, 'maintence_record.html', {'records':records})

def createMaintenceRecord(request):
    if request.method == 'POST':
        form = MaintencRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)  
            
            record.save()  
            return redirect('maintence_records')
    else:
        form = MaintencRecordForm()  
    
    context = {'form': form}
    return render(request, 'create_maintence_record.html', context)



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