from django.contrib import admin
from .models import Company, CompanyDetails, Address


class CompanyDetailsAdmin(admin.StackedInline):
    model = CompanyDetails


class AddressAdmin(admin.StackedInline):
    model = Address



@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        AddressAdmin,
        CompanyDetailsAdmin, 
    ]
