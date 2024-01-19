from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=250)
    review = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=250)
    date = models.CharField(max_length=150)
    time = models.CharField(max_length=150)
    party_size = models.CharField(max_length=150)
    special_requests = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

#model review
#user
#reservations

