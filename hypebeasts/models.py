from django.db import models

class Hypebeast(models.Model):
    clothing = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
 