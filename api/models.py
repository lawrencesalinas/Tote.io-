from email.mime import image
from django.db import models
from django.contrib.auth.models import User
# Create your models herez 

class Produt(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True) 
    # image = 
    brand = models.CharField(max_length=200, null=True, blank=True) 
    castegory = models.CharField(max_length=200, null=True, blank=True) 
    # null = True even with no user id, blank = true fill up a form not have to fill it up
    description = models.TextField(null=True, blank=True) 
    rating = models.DecimalField(max_digits=7, decimal_places=2)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
