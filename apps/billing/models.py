from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=40, unique=True, blank=True)
    code = models.CharField(max_length=2, blank=True)  # not unique as there are duplicates (IT)

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ("name",)

    def __str__(self):
        return "%s" % (self.name or self.code)


class State(models.Model):
    name = models.CharField(max_length=165, blank=True)
    code = models.CharField(max_length=8, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="states")

    class Meta:
        unique_together = ("name", "country")
        ordering = ("country", "name")

    def __str__(self):
        txt = self.to_str()
        country = "%s" % self.country
        if country and txt:
            txt += ", "
        txt += country
        return txt

    def to_str(self):
        return "%s" % (self.name or self.code)
