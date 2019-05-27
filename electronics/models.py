from django.db import models


class Electronics(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name