from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_committee = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profile_pics', blank=True)
    

class Welcome(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Info(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    caroussel_position = models.IntegerField(default=0)
    caroussel_image = models.ImageField(upload_to='caroussel_images', blank=True, null=True)

    def __str__(self):
        return self.title