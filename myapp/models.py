from django.db import models

# Create your models here.
class User_service(models.Model):
    name = models.CharField(max_length=70)
    service = models.CharField(max_length=120)
    service_man = models.CharField(max_length=70)
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    cost = models.IntegerField()