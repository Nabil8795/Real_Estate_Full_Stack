from django.db import models

# Create your models here.

class Property(models.Model):
    name = models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    detail = models.CharField(max_length=500)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name