from asyncio.windows_events import NULL
import datetime
from django.db import models
from django.contrib.auth.models import User

from embed_video.fields import EmbedVideoField

# Create your models here.
class superuser(models.Model):
    user = models.OneToOneField(User, null = True, blank = True, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    bio = models.TextField()
    #login = models.CharField(max_length=100)
    profile_img = models.ImageField(null = True, blank = True)




class posts(models.Model):
    title = models.CharField(unique= True, max_length=100)
    body = models.TextField()
    createdOn = models.CharField(max_length=100)
    url = EmbedVideoField()
    # default="https://www.youtube.com/watch?v=JeSLBEYK7cs"

    def __str__(self):
        return self.title
