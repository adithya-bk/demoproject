from django.contrib import admin

from shop.models import Product, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
