from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    skin_type  = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=1000)
    purpose = models.CharField(max_length=100)
    category = models.CharField(max_length=100, null=True)
    price = models.IntegerField()


    def __str__(self):
        return self.name  # product name
    
