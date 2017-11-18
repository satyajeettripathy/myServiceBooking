from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Appointment,Customer,Service
import json
import datetime
from django.utils.text import phone2numeric
from .EmailService import *
'''
API support
1. Fetch 
2. Fetch free slots for a day
3. Fetch bookings for a day
4. Fetch bookings for a existing user

'''
from django.http.response import JsonResponse, HttpResponse

# Method 1 : GetAllMfg

def getAllBookings(request):
    bs=[]
    bookings = Appointment.objects.all()
    for booking in bookings:
        bs.append(booking)
    return HttpResponse(json.dumps(bs),content_type='application/json')

def getAllBookingsByDate(request):
    bs=[]
    date_range_start=request.GET.get('start_date')
    dt_start=datetime.datetime.strptime(date_range_start,'%Y-%m-%d')
    date_range_end=request.GET.get('end_date')
    dt_end=datetime.datetime.strptime(date_range_end,'%Y-%m-%d')+datetime.timedelta(days=1)
    bookings=Appointment.objects.all()
    bookings=bookings.filter(serviceDate_gt=dt_start)
    bookings=bookings.filter(serviceDate_lt=dt_end)
    for booking in bookings:
        bs.append(booking.to_dict())
    return HttpResponse(json.dumps(bs),content_type='application/json')

@csrf_exempt
def bookAppointment(request):
    in_data=None
    customer=None
    if(request.method=='POST'):
        in_data=json.loads(request.body())
    if('customer' in in_data.keys()):
        customer=getOrCreateCustomer(in_data['customer'])
    a=Appointment.objects.create()
    a.customer=customer
    s=Service.objects.get(type=in_data['service_type'])
    a.service=s
    a.serviceInstructions=in_data['serviceInstruction']
    a.serviceDateTime=datetime.datetime.strptime(in_data['dateTime'],'%Y-%m-%d %H-%M-%S')
    a.save()
    mail={'Subject':'Booking complete'}
    sendConfirmationMail(mail)
    return HttpResponse(json.dumps(a.to_dict()),content_type='application/json')
    

def getOrCreateCustomer(customer):
    email=None
    phone=None
    if('email' in customer.keys()):
        email=customer['email']
    if('phoneNumber' in customer.keys()):
        phone=customer['phoneNumber']
    if(email==None and phone==None):
        return None
    customers=Customer.objects.all()
    if(email != None and email !=""):
        customers=customers.filter(email_iexact=email)
    if(phone != None and phone!=""):
        customers=customers.filter(email_iexact=email)
    if(len(customers)==0):
        c=Customer.objects.create()
        if('name' in customer.keys()):
            c.name=customer['name']
        if(phone!=None):
            c.phoneNumber=phone
        if(email!=None):
            c.email=email
        c.save()
        return c
    else:
        return customers.first().to_dict()
        
        
    
    
    
    
        
    
     


# Create your views here.
