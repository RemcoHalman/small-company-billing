from django.db import models
import datetime

class Invoice(models.Model):
    invoice_title = models.CharField(max_length=200)
    invoice_number = models.IntegerField(default=0)
    invoice_state = models.ForeignKey(
        'common.InvoiceState',
        on_delete=models.PROTECT,
        related_name="invoice_state"
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
    )
    tax_value = models.ForeignKey(
        'common.Tax',
        on_delete=models.PROTECT,
        related_name="invoice_tax",
        default=1
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