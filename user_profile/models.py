from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserGenralProfile(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=255,blank=False)
    last_name = models.CharField(max_length=255,blank=True, null=True)
    dob = models.DateField(null=True)
    address = models.TextField(null=True)
    profile_img = models.ImageField(upload_to='profileImage',null=True)
    phone_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name}__{self.user}'
    

class UserMedicalProfile(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.SET_NULL, null=True)
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name}__{self.user}'
    
    

    # wieght 
    # height
    # blood gropu
    # bmi#
    # eyes sight
    # plateltates
    # phylicl siablitites   