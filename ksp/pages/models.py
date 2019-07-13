from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django import forms
# Create your models here.
class Database(models.Model):

    criminal_name = models.CharField(max_length = 20) 
    criminal_img = models.ImageField(upload_to = 'database')
    encodings = ArrayField(ArrayField(models.FloatField(max_length = 1000, null = True)))

class Search(models.Model):
    
    criminal_name = models.CharField(max_length = 20) 
    criminal_img = models.ImageField(upload_to = 'search')  
