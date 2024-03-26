from django.db import models

from marketplace.models.product import Product


class SaleHistory(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="sale_histories"
    )
    owner = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="sale_histories"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_unit = models.CharField(max_length=10, default="sol")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    buyer = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="purchased_products"
    )

    def __str__(self):
        return f"{self.owner.username} sold {self.product.name} to {self.buyer.username} for {self.price} {self.price_unit}"
