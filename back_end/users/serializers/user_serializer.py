from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    wallets = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "wallets",
        ]

    def get_wallets(self, obj):
        wallets = obj.wallet_set.all()
        data = []
        for wallet in wallets:
            data.append(
                {
                    "id": wallet.id,
                    "public_key": wallet.public_key,
                    "wallet_type": wallet.wallet_type,
                }
            )
        return data
