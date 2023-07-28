from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'weight', 'color', 'amount', 'discription']

admin.site.register(Product, ProductAdmin)