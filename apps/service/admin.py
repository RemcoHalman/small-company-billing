from django.contrib import admin
from .models import Product, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass
    # list_display = ()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
    # list_display = ()
