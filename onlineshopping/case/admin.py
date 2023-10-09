from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Product)
admin.site.register(Category)
