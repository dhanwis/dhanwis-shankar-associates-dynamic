from django.db import models

# Create your models here.

class Project(models.Model):
    image = models.ImageField(upload_to='admin_app/projects')
    head = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)

class Message(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    message = models.CharField(max_length=1000)