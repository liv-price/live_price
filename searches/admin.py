from django.contrib import admin
from .models import ProductData

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name' , 'update_date')
    ordering = ('product_name' ,)
    search_fields = ('product_name' ,)

admin.site.register(ProductData, ProductAdmin)