from django.contrib import admin
from .models import Brand,Car,Kit,KitCarRelation,Manufacturer

class ManufacturerAdmin(admin.ModelAdmin):
    fields=[('name'),'created_by','updated_by']
    list_display = ('id','name', 'created_at')
    
admin.site.register(Manufacturer,ManufacturerAdmin)

class BrandAdmin(admin.ModelAdmin):
    fields=['name','manufacturer','created_by','updated_by']
    list_display=('id','name','manufacturer','created_by')
admin.site.register(Brand,BrandAdmin)

class CarAdmin(admin.ModelAdmin):
    fields=['brand','variant_name','description','launch_date','created_by','updated_by']
    list_display=('id','brand','variant_name','description','launch_date')

admin.site.register(Car,CarAdmin)

class KitAdmin(admin.ModelAdmin):
    fields=['name','created_by','updated_by']
    list_display=('name','created_by','updated_by')

admin.site.register(Kit,KitAdmin)

class KitCarRelationAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,{'fields':['car','kit','created_by','updated_by']}),
        ('Validity Period',{'fields':['startDate','endDate']}),
        ]
    list_display=('car','kit','created_by','updated_by','startDate','endDate')
admin.site.register(KitCarRelation,KitCarRelationAdmin)



# Register your models here.
