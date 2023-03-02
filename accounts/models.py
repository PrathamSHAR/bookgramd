from django.db import models

# Create your models here.


class Address(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=200)
    age=models.IntegerField( blank=True ,null=True)



class Signup(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=14)
    

  


