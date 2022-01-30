import imp
from re import T
from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name= 'profile', null=True, blank=True)
    profile_img = models.ImageField(blank=True, null= True)
    skill = models.CharField(max_length= 40, blank=True, null=True)
    friends = models.ManyToManyField(User, related_name='friends', blank=True, null=True)
    status = models.TextField(default= 'This User is busy')
    # birthday = models.DateField(default='2000-03-20')

def __str__(self):
    return f"{self.user}'s profile"