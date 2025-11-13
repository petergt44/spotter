from django.db import models

class FuelPrice(models.Model):
    state = models.CharField(max_length=50)
    price_per_gallon = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.state}: {self.price_per_gallon}"
