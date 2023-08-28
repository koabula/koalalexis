from django.db import models

# Create your models here.
class invitecode(models.Model):
    code=models.CharField(max_length=200)