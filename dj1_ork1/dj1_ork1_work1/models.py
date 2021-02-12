from django.db import models

# Create your models here.
class aticlename(models.Model):
    nameDB = models.CharField(max_length=50)
    insideDB = models.TextField()