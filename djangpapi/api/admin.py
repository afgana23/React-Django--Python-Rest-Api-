from django.contrib import admin
from .models import Customer


@admin.register(Customer)
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id',"c_name",'phone','age','gender']
