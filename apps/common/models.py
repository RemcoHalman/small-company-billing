from django.db import models
from django.core.exceptions import ValidationError


class Priority(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Priority Choices"


class InvoiceState(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Invoice Status"


class Tax(models.Model):
    value = models.PositiveIntegerField()
    tax_value = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        editable=False
    )

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name_plural = "Taxes"

    def save(self):
        self.validate_ratio(self.value)
        self.tax_value = self.convert_to_percentage(self.value)
        super(Tax, self).save()

    def validate_ratio(self, value):
        try:
            if not (0 <= value <= 100):
                raise ValidationError(
                    f'{value} must be between 0 and 100',
                    params={'value': value}
                )
        except TypeError:
            raise ValidationError(
                f'{value} must be a number', params={'value': value}
            )

    def convert_to_percentage(self, value):
        percentage = value / 100
        return percentage

class DueDate(models.Model):
    time_due_date = models.PositiveIntegerField(
        unique=False,
        blank=False,
    )

    def __str__(self):
        return str(self.time_due_date)
