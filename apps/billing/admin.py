from django.contrib import admin
from .models import Country, State


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', )


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'country', )
