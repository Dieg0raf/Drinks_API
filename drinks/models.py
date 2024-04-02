from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=100)
    size = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name