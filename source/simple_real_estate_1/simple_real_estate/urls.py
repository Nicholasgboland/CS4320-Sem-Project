"""
URL configuration for simple_real_estate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from real_estate import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    #path('', views.index, name='login'),
    path('properties/', views.properties, name = 'properties_list'),
    path('property/update/<int:pk>/', views.updateProperty, name='update_property'),
    path('property/<int:pk>/delete/', views.delete_property, name='delete_property'),
    path('properties/property_form/', views.createProperty, name = 'property_form'),
    
    path('properties/<int:pk>/units/', views.units, name = 'units_list'),
    path('properties/unit_form/', views.createUnit, name = 'unit_form'),


    path('properties/units/<int:pk>/rental_agreement', views.rentalAgreement, name = 'rental_agreement_list'),
    path('properties/units/rental_agreement_form/<int:pk>', views.createRentalAgreement, name = 'rental_agreement_form'),


    path('properties/units/rental_agreement/<int:pk>/rental_invoice', views.rentalInvoice, name = 'rental_invoice_list'),



    path('tenants/', views.tenant, name = 'tenant_list'),
    path('tenants/tenate_form/', views.createTenant, name = 'tenant_form' ),




    path('maintence_form/<int:pk>', views.createMaintenceRecord, name = 'maintence_form'),


    path('maintence_records/<int:pk>', views.maintence_record, name = 'maintence_records'),
]
