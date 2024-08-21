from django.contrib import admin
from . import models
from core.models import User as u

# customize list page 
@admin.register(models.Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display=['namear','nameen','user','descar','fun_display']
    list_editable=['descar']
    list_per_page=10
    def fun_display(self,hotel):
        if(hotel.stars > 2):
            return 'low'
        return 'good'
@admin.register(u)
class UsersAdmin(admin.ModelAdmin):
    # list_display=['namear','nameen','user','descar','fun_display']
    # list_editable=['descar']
    list_per_page=10
    def fun_display(self,hotel):
        if(hotel.stars > 2):
            return 'low'
        return 'good'    
# Register your models here.
# admin.site.register(models.Hotel)