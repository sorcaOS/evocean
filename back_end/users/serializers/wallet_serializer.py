from rest_framework import serializers

from users.models.wallet import Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ["public_key", "wallet_type"]

    def save(self, user, **kwargs):
        wallet_type = self.validated_data.get("wallet_type")
        if wallet_type:
            wallet, _ = Wallet.objects.get_or_create(
                user=user,
                public_key=self.validated_data["public_key"],
                wallet_type=wallet_type,
            )
        else:
            wallet, _ = Wallet.objects.get_or_create(
                user=user, public_key=self.validated_data["public_key"]
            )
        wallet.save()
        return wallet
