from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=160)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name
