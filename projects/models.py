from django.db import models
from authors.models import Author
from django.db.models import SET_NULL 

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    techology =  models.CharField(max_length=200) 
    createdAt = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete = SET_NULL, null=True, related_name="author")