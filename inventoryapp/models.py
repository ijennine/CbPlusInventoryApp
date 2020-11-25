from django.db import models

# Create your models here.
class Product(models.Model):
    reference = models.AutoField(primary_key=True)
    product_gtin = models.BigIntegerField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.product_gtin

    def __eq__(self, other):
        if self.product_gtin == other.product_gtin:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.product_gtin > other.product_gtin:
            return True
        else:
            return False

    def __le__(self, other):
        if self.product_gtin > other.product_gtin:
            return True
        else:
            return False