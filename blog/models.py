from django.db import models

# Create your models here.

class Blogs(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    brief=models.TextField(default="This is a brief")