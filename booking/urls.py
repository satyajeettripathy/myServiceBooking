'''
Created on Nov 13, 2017

@author: Satyajeet
'''

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.getAllBookings,name='AllBookings'),
    url(r'^AppointmentsByDate$',views.getAllBookingsByDate,name='AppointmentsByDate')
    ]
