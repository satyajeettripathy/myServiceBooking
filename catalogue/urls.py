'''
Created on Nov 13, 2017

@author: Satyajeet



'''
from django.conf.urls import url
from . import views 

#app_name='catalogue'

urlpatterns=[
    url(r'^Manufacturers/$',views.getAllManufacturers,name='Manufacturers'),
    url(r'^MapKitCar$',views.addRelationship,name='MapKitCar'),
    url(r'^Brands$',views.getAllBrands,name='Brands'),
    url(r'^Cars$',views.getAllCars,name='Cars'),
    url(r'^Manufacturers/(?P<mName>[a-zA-Z0-9_]+)/Brands/$',views.getAllBrandsByManufacturer,name='BrandsByManufacturer'),
    url(r'^Manufacturers/(?P<mName>[a-zA-Z0-9_]+)/Brands/(?P<bName>[a-zA-Z0-9_]+)/$',views.getAllCarVariantByBrand,name='CarsByBrand'),
    url(r'^Relations$',views.getAllRelations,name='Relations')
    ]

#^(?P<question_id>[0-9]+)/vote/$