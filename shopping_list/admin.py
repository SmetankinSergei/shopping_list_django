from django.contrib import admin

from shopping_list.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'details', 'category', 'img', 'price']
    list_editable = ['name', 'details', 'category', 'img', 'price']
