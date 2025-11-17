from django.db import models
from Users.models import User
from Products.models import Products

# Create your models here.
class UserActivity(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id  = models.ForeignKey(Products, on_delete=models.CASCADE)
    event_type  = models.CharField(max_length=50)
    rating = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)