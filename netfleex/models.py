from pyexpat import model
from turtle import title
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICES(
    ('All','All')
    ('Kids','Kids')
)
# Create your models here.
class CustomUser(AbstractUser):
    profiles=models.ManyToManyField('Profile',null=True,blank=True)

class Profile(models.Model):
    name=models.CharField(max_length=225)
    age_limit=models.CharField(max_length=10,choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4)

class Movie(models.Model):
    title=models.CharField(max_length=225)
    description=models.TextField(blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    