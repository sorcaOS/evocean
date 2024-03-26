from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class BaseViewSet(viewsets.ModelViewSet):
    """
    Base ViewSet for all ViewSets
    """

    permission_classes = [AllowAny]

    response = Response
