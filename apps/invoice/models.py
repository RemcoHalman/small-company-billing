from django.db import models
from django.forms.models import ModelForm
import datetime
from apps.account.models import CustomUser
from apps.service.models import Service, Product
from django.forms.widgets import CheckboxSelectMultiple


class Invoice(models.Model):
    invoice_title = models.CharField(max_length=200)
    invoice_number = models.IntegerField(default=0)
    invoice_state = models.ForeignKey(
        'common.InvoiceState',
        on_delete=models.PROTECT,
        related_name="invoice_state",
        default=1
    )
    to_address = models.ForeignKey(
        'customer.Address',
        on_delete=models.PROTECT,
        related_name="invoice_to_address"
    )
    created_by = models.ForeignKey(
        'account.CustomUser',
        related_name="invoice_created_by",
        on_delete=models.SET_NULL,
        null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    due_date = models.ForeignKey(
        'common.DueDate',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        default=3
    )
    product = models.ManyToManyField(
        'service.Product',
        related_name='product',
        blank=True,
    )
    service = models.ManyToManyField(
        'service.Service',
        related_name='service',
        blank=True,
    )

    def __str__(self):
        return self.invoice_title

    def save(self):
        if not self.invoice_number:
            self.invoice_number = self.invoice_id_generator()
            while Invoice.objects.filter(
                invoice_number=self.invoice_number
            ).exists():
                self.invoice_number = self.invoice_id_generator(
                    prev_invoice_number=self.invoice_number
                )
        super(Invoice, self).save()

    def invoice_id_generator(self, prev_invoice_number=None):
        if prev_invoice_number:
            number = int(prev_invoice_number)
            number += 1
            return number
        year = datetime.datetime.today().year
        return f"{year}{1:04d}"

# class CheckboxForm(ModelForm):
#     class Meta:
#         model = Invoice
#         fields = ("service", "product", )

#     def __init__(self, * args, ** kwargs):
#         super(CheckboxForm, self).__init__( * args, ** kwargs)

#         self.fields["service"].widget = CheckboxSelectMultiple()
#         self.fields["service"].queryset = Service.objects.all()
#         self.fields["product"].widget = CheckboxSelectMultiple()
#         self.fields["product"].queryset = Product.objects.all()