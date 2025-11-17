from django.db import models

# Create your models here.

class Items(models.Model):
    product_name = models.CharField(max_length=100)
    views = models.BigIntegerField(default=0)
    clicks = models.IntegerField(default=0)
    purchases = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name
    
