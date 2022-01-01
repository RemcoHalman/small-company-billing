from django.contrib import admin
from .models import Customer, CustomerDetails, Address


class CustomerDetailsAdmin(admin.StackedInline):
    model = CustomerDetails


class AddressAdmin(admin.StackedInline):
    model = Address


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [
        AddressAdmin,
        CustomerDetailsAdmin,
    ]
