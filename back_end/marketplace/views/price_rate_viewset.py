from rest_framework import serializers

from marketplace.models.pricate_rate import PriceRate
from src.controllers.price_rate_controller import PriceRateController
from src.entities.base_viewset import BaseViewSet


class PriceRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceRate
        fields = "__all__"


class PriceRateViewSet(BaseViewSet):
    queryset = PriceRate.objects.all()
    serializer_class = PriceRateSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        price_rate_controller = PriceRateController()
        rate = price_rate_controller.fetch_price_rate(
            from_currency=instance.price_unit, to_currency=instance.target_currency
        )
        if rate is not None:
            instance.price = str(rate)
            instance.save()
        serializer = self.get_serializer(instance)
        return self.response(data=serializer.data, status=200)
