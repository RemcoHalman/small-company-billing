from django.contrib import admin
from .models import Tax, DueDate, Country, State


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('tax_option',)


@admin.register(DueDate)
class DueDateAdmin(admin.ModelAdmin):
    list_display = ('time_due_date',)



@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name','code',)


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'country',)
