from .models import Manufacturer,Car,Kit,KitCarRelation,Brand
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,get_object_or_404
import json,re,datetime,calendar
from django.http.response import HttpResponse,JsonResponse
from .Util import months
#from Service import *

# Create your views here.
'''
API to support
1.add relation
2.get all MFG
3.Get all Brand given a MFG
4.Get all Brand paginated
5.Get all car given a brand
6.Get all car paginated
7.update relation
8.Delete relation

'''

# Manufacturer Section
 
def getAllManufacturers(request):
    listM=[]
    for m in Manufacturer.objects.all():
        listM.append(m.to_dict())
    response = HttpResponse(json.dumps(listM),content_type='application/json')
    return response


# Brand Section

def getAllBrands(request):
    listBrand=[]
    for b in Brand.objects.all():
        listBrand.append(b.to_dict())
    return HttpResponse(json.dumps(listBrand),content_type='application/json')

def getAllBrandsByManufacturer(request,mName):
    #return HttpResponse(mName)
    listBrand=[]
    m = get_object_or_404(Manufacturer,name=mName)
    for b in m.brand_set.all():
        listBrand.append(b.to_dict())
    return HttpResponse(json.dumps(listBrand),content_type='application/json')
        

#Car Section
def getAllCars(request):
    listCars=[]
    for b in Car.objects.all():
        listCars.append(b.to_dict())
    return HttpResponse(json.dumps(listCars),content_type='application/json')

def getAllCarVariantByBrand(request,bName,mName):
    #return HttpResponse(mName+bName)
    listCars=[]
    man= get_object_or_404(Manufacturer,name=mName)
    br = man.brand_set.all().get(name=bName)
    cars =br.car_set.all()
    for car in cars:
        listCars.append(car.to_dict())
    return HttpResponse(json.dumps(listCars),content_type='application/json')
    
#Relation Section
#Paginated
@csrf_exempt
def getAllRelations(request):
    #print("hello"+request.body)
    in_data=json.loads(request.body)
    resultSet=getRelationsByFilter(in_data)
    resultList=[]
    for result in resultSet:
        resultList.append(result.to_dict())
    return HttpResponse(json.dumps(resultList),content_type='application/json')
    #Prepare a car list based on subset of mfg/brand/car
   
    #carList.append(getCarList(manList,brandList,carList)) 

@csrf_exempt
def addRelationship(request):
    if request.method=='POST':
        in_data = json.loads(request.body)
        carList=[]
        try:
            if 'brand' in in_data.keys():
                i_brand=get_object_or_404(Brand,pk=in_data['brand'])
                for c in i_brand.car_set.all():
                    carList.append(c)
            if 'car' in in_data.keys():
                carList.append(get_object_or_404(Car,pk=in_data['car']))
            i_kit=get_object_or_404(Kit,pk=in_data['kit'])
            
            validity=in_data['validity']
        except KeyError:
            return HttpResponse("Key Error Please check documentation")
        
        pattern=re.compile('[0-9]{2}:[0-9]{4},[0-9]{2}:[0-9]{4}')
        if pattern.match(validity) is None:
            return HttpResponse('Incorrect Data Format')
        
        map=parseIntoDate(in_data['validity'])
        for c in  carList:
            rel= setDataForRelation(c,i_kit,map['start'],map['end'])
            rel.save()
        response=  HttpResponse("Update Success")
        
    return response

def parseIntoDate(dateStr):
    
    #formate MON:YYYY,MON:YYYY
    #[0-9]{2}:[0-9]{4},[0-9]{2}:[0-9]{4}
    dates={}
    (st,en) = dateStr.split(',',1)
    (st_mon,st_yr)=st.split(':',1)
    (en_mon,en_yr)=en.split(':',1)
    dates['start'] =  datetime.date(int(st_yr),int(st_mon),1)
    (mon_st,mon_en)=calendar.monthrange(int(en_yr), int(en_mon))  
    dates['end']= datetime.date(int(en_yr),int(en_mon),mon_en) 
    return dates


def setDataForRelation(car_id,kit_id,st,en):
    rel = KitCarRelation()
    rel.carid=car_id
    rel.kitid=kit_id
    rel.startDate=st
    rel.endDate=en
    rel.created_by='satyajeet'
    rel.updated_by='satyajeet'
    return rel

def getRelationsByFilter(in_data):
    manList=[]
    brandList=[]
    carList=[]
    kitList=[]
    start_date=None
    end_date=None
    if('mfg' in in_data.keys()):
        manList=in_data['mfg']
    if('brand' in in_data.keys()):
        brandList=in_data['brand']
    if('car' in in_data.keys()):
        carList=in_data['car']
    if('start_date' in in_data.keys()):
        start_date=in_data['start_date']
    if('end_date' in in_data.keys()):
        end_date=in_data['end_date']
    if('kit' in in_data.keys()):
        kitList=in_data['kit']
    
       
    set_car=Car.objects.all()
    if(len(manList)>0):
        set_car=set_car.filter(brand__manufacturer__id__in=manList)
    if(len(brandList)>0):
        set_car=set_car.filter(brand__id__in=brandList)
    if(len(carList)>0):
        set_car=set_car.filter(id__in=carList)
    final_car_list=[]
    for car in set_car:
        final_car_list.append(car.id)
    
    rels = KitCarRelation.objects.all()
    if(len(final_car_list)>0):
        rels=rels.filter(carid__id__in=final_car_list)
    if(len(kitList)>0):
        rels=rels.filter(kitid__id__in=kitList)
    if(start_date!=None):
        start_date=datetime.datetime.strptime(start_date)
        rels=rels.filter(startDate_gt=start_date)
    if(end_date!=None):
        end_date=datetime.datetime.strptime(end_date)
        rels=rels.filter(endDate_lt=end_date)
    
    return rels
