from django.db import models
from django.contrib.auth.models import User

class Profilecheck(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.SET_NULL, null=True)
    profile_exist = models.BooleanField(default=False)