from django.contrib import admin
from .models import Tax, DueDate, Priority, InvoiceState


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('value', 'tax_value')


@admin.register(DueDate)
class DueDateAdmin(admin.ModelAdmin):
    list_display = ('time_due_date',)


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    pass


@admin.register(InvoiceState)
class InvoiceStateAdmin(admin.ModelAdmin):
    pass
