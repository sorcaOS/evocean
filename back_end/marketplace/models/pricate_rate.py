from django.db import models


class PriceRate(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_unit = models.CharField(
        max_length=10, default="solana", unique=True, primary_key=True
    )
    target_currency = models.CharField(max_length=10, default="usd")

    def __str__(self):
        return f"{self.price} {self.price_unit}"
