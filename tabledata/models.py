from django.db import models

# Create your models here.
class insertdata(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=12)
    city=models.CharField(max_length=50)