from django.db import models

# Create your models here.

class Contact(models.Model):
    number=models.CharField(max_length=120)