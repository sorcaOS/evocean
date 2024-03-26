from rest_framework import serializers

from marketplace.models import TemplateFormat
from marketplace.models.product import Product
from src.entities.base_viewset import BaseViewSet


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateFormat
        exclude = ["theme"]


class ProductSerializer(serializers.ModelSerializer):
    sale_histories = serializers.SerializerMethodField()
    formats = FormatSerializer(many=True, source="template_formats")

    class Meta:
        model = Product
        fields = "__all__"
        depth = 1

    def get_sale_histories(self, obj):
        sale_histories = obj.sale_histories.all().count()
        return sale_histories


class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all().order_by("-id")
    serializer_class = ProductSerializer
    filterset_fields = ["category", "owner", "is_day_and_night_mode", "is_featured"]
