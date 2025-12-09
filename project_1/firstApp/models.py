from django.db import models

# Create your models here.

class person(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(default="")
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)