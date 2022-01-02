from django.contrib import admin
from django.db import models
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from .models import Invoice
from apps.account.models import CustomUser


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'invoice_title',
        'created_by',
        'invoice_state',
        'invoice_number',
    )
    exclude = (
        'invoice_number',
        'created_by',
    )
    formfield_overrides = {
        models.ManyToManyField: {
            'widget': forms.CheckboxSelectMultiple
        },
    }
    change_form_template = "invoice/preview_invoice.html"
    
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        print(obj.created_by)
        super(InvoiceAdmin, self).save_model(request, obj, form, change)

    def response_change(self, request ,obj):
        if "_preview" in request.POST:
            matching_names_except_this = self.get_queryset(request).filter(invoice_title=obj.invoice_title).exclude(pk=obj.id)
            matching_names_except_this.delete()
            obj.save()
            self.message_user(request, "Saved and opening preview")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)
