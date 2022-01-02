from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(
        null=True,
        blank=True,
        max_length=150,
        help_text="Service description max length 150 characters"
    )
    price_per_hour = models.DecimalField(
        decimal_places=2,
        max_digits=4,
        default=42.50,
        help_text="Default has been set to €42,50"
    )
    hours = models.TimeField(
        help_text="Time spend for doing the service",
        default='1:00'
    )
    tax_value = models.ForeignKey(
        'common.Tax',
        on_delete=models.PROTECT,
        related_name="service_tax",
        default=3
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(
        null=True,
        blank=True,
        max_length=150,
        help_text="Product description max length 150 characters"
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=4,
        default=10.00,
        help_text="Price per product, price without TAX. This will be automatically added"
    )
    tax_value = models.ForeignKey(
        'common.Tax',
        on_delete=models.PROTECT,
        related_name="product_tax",
        default=3
    )

    def __str__(self):
        return self.name
