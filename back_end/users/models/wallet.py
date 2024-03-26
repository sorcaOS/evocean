from django.db import models


class Wallet(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    public_key = models.CharField(max_length=255)

    class WalletTypeChoices(models.TextChoices):
        PHANTOM = "PHANTOM", "Phantom"

    wallet_type = models.CharField(
        max_length=255,
        choices=WalletTypeChoices.choices,
        default=WalletTypeChoices.PHANTOM,
    )
