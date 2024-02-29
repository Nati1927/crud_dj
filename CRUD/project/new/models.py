from django.db import models

# Create your models here.
class Member(models.Model):
    First_name=models.CharField(max_length = 20)
    Last_name = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20)
