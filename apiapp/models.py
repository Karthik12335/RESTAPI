from django.db import models

# Create your models here.

class Studentinfo(models.Model):
    name=models.CharField(max_length=50)
    rno=models.IntegerField()
    per=models.FloatField()
