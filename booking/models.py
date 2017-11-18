from django.db import models
from django.db.models.deletion import DO_NOTHING



# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=500)
    email=models.EmailField(max_length=500)
    phoneNumber=models.CharField(max_length=20)
    created_at=models.DateField(auto_now_add=True)
    created_by=models.CharField(max_length=200, db_index=True)
    updated_at=models.DateField(auto_now=True)
    updated_by=models.CharField(max_length=10)
    def to_dict(self):
        d={}
        d['name']=self.name
        d['email']=self.email
        d['phoneNumber']=self.phoneNumber
        return d

class Service(models.Model):
    type=models.CharField(max_length=10)
    description=models.CharField(max_length=500)
    time=models.IntegerField(default=2)
    cost_per_hr=models.IntegerField(default=100)
    created_at=models.DateField(auto_now_add=True)
    created_by=models.CharField(max_length=200, db_index=True)
    updated_at=models.DateField(auto_now=True)
    updated_by=models.CharField(max_length=10)
    def to_dict(self):
        d={}
        d['type']=self.type
        d['description']=self.description
        d['time']=self.time
        d['cost_per_hr']=self.cost_per_hr
        return d
    
class Appointment(models.Model):
    customer=models.ForeignKey('Customer',on_delete=DO_NOTHING)
    service=models.ForeignKey('Service',on_delete=DO_NOTHING)
    serviceInstruction=models.CharField(max_length=500)
    serviceDateTime=models.DateTimeField
    created_at=models.DateField(auto_now_add=True)
    created_by=models.CharField(max_length=200, db_index=True)
    updated_at=models.DateField(auto_now=True)
    updated_by=models.CharField(max_length=10)
    
    def to_dict(self):
        d={}
        d['customer']=self.customer.to_dict()
        d['type']=self.serviceType.to_dict()
        d['instructions']=self.serviceInstruction
        d['datetime']=self.serviceDate
        return d