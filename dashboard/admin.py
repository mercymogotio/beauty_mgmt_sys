from django.contrib import admin
from dashboard.models import *

# Register your models here.
class AdminProducts(admin.ModelAdmin):
    list_display = ['name','price']

class AdminStaffs(admin.ModelAdmin):
    list_display = ['name','email','mobile', 'password']

class AdminRatings(admin.ModelAdmin):
    list_display = ['rating','review']

admin.site.register(Product, AdminProducts)
admin.site.register(Staff, AdminStaffs)
admin.site.register(Rating, AdminRatings)