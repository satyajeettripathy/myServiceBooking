from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.
'''
funtions
1. Fetch/update list of manufacturers
2. Fetch/update list of brands
3. Fetch/update list of kit
4. Random text

'''

class Manufacturer(models.Model):
    name=models.CharField(max_length=200, db_index=True)
    created_at=models.DateField(auto_now_add=True)
    created_by=models.CharField(max_length=200, db_index=True)
    updated_at=models.DateField(auto_now=True)
    updated_by=models.CharField(max_length=10)
    def __str__(self):
        return self.name
    def to_dict(self):
        d={}
        d['name']=self.name
        return d

class Brand(models.Model) :
    name=models.CharField(max_length=200, db_index=True)
    manufacturer=models.ForeignKey('Manufacturer',on_delete=DO_NOTHING)
    created_at=models.DateField(auto_now_add=True)
    created_by=models.CharField(max_length=200, db_index=True)
    updated_at=models.DateField(auto_now=True)
    updated_by=models.CharField(max_length=10)
    def __str__(self):
        return self.name
    def to_dict(self):
        d={}
        d['name']=self.name
        d['manufacturer']=self.manufacturer.to_dict()
        return d
    
class Car(models.Model):
    brand=models.ForeignKey('Brand',on_delete=DO_NOTHING)
    variant_name=models.CharField(max_length=200,db_index=True,blank=True)
    description=models.CharField(max_length=500,blank=True)
    launch_date=models.DateField(blank=True)
    created_at=models.DateField(auto_now_add=True)
    created_by=models.CharField(max_length=200, db_index=True)
    updated_at=models.DateField(auto_now=True)
    updated_by=models.CharField(max_length=10)
    def __str__(self):
        return self.variant_name
    def to_dict(self):
        d={}
        d['brand']=self.brand.to_dict()
        d['variant_name']=self.variant_name
        d['description']=self.description
        return d
    
    
class Kit(models.Model):
    name=models.CharField(max_length=200,db_index=True)
    created_at=models.DateField(auto_now_add=True)
    created_by=models.CharField(max_length=200, db_index=True)
    updated_at=models.DateField(auto_now=True)
    updated_by=models.CharField(max_length=10)
    def __str__(self):
        return self.name
    def to_dict(self):
        d={}
        d['name']=self.name
        return d

class KitCarRelation(models.Model):
    
    car=models.ForeignKey('Car',on_delete=DO_NOTHING)
    kit=models.ForeignKey('Kit',on_delete=DO_NOTHING)
    startDate=models.DateField(null=False,blank=False)
    endDate=models.DateField(null=False,blank=False)
    created_at=models.DateField(auto_now_add=True)
    created_by=models.CharField(max_length=200, db_index=True)
    updated_at=models.DateField(auto_now=True)
    updated_by=models.CharField(max_length=10)
    def to_dict(self):
        d={}
        d['car']=self.car.to_dict()
        d['kit']=self.kit.to_dict()
        d['starDate']=self.startDate
        d['endDate']=self.endDate
        return d

    
    
