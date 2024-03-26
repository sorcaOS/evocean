from rest_framework import routers

from marketplace.views.price_rate_viewset import PriceRateViewSet
from marketplace.views.product_viewset import ProductViewSet

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"price", PriceRateViewSet)
