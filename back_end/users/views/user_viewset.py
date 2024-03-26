from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.decorators import action

from src.entities.base_viewset import BaseViewSet
from users.serializers.user_serializer import UserSerializer
from users.serializers.wallet_serializer import WalletSerializer


class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["get"]

    @action(detail=True, methods=["get"], url_path="avatar")
    def avatar(self, request, pk=None):
        user: User = self.get_object()
        avatar = user.auth_profile.photo_url
        return self.response(avatar, status=200)

    @action(
        detail=False,
        methods=["POST"],
        url_path="add_wallet",
        serializer_class=WalletSerializer,
        http_method_names=["post"],
    )
    def add_wallet(self, request, pk=None):
        user: User = request.user
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        wallet = serializer.save(user=user)
        data = self.serializer_class(wallet).data
        return self.response(data, status=201)
