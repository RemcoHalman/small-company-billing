from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CompanyDetails(models.Model):
    company = models.OneToOneField(
        Company,
        on_delete=models.PROTECT
    )
    IBAN_number = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        help_text="Bank account number",
    )
    vat_number = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        help_text="VAT number / BTW nummer",
    )
    register_number = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        help_text="Chamber of Commerce / KVK nummer",
    )
    

    def __str__(self):
        return f"{self.company}"


class Address(models.Model):
    company = models.OneToOneField(
        Company,
        on_delete=models.PROTECT
    )
    country = models.OneToOneField("billing.Country", on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=64)
    address_line_2 = models.CharField(
        max_length=64,
        blank=True,
        null=True
    )
    house_number = models.IntegerField()
    appartment_addition = models.CharField(
        max_length=64,
        blank=True,
        null=True
    )
    zip_code = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.company}"