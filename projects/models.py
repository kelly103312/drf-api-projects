from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    techology =  models.CharField(max_length=200) 
    createdAt = models.DateTimeField(auto_now_add=True)
    