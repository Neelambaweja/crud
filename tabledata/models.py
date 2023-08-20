from django.db import models

# Create your models here.
class insertdata(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=12)
    city=models.CharField(max_length=50)


class helpdata(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=12)
    msg=models.CharField(max_length=50)