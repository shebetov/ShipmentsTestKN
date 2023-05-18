from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from catalog.serializers import ItemSerializer
from .models import Country, City, Shipment
from .serializers import CountrySerializer, CitySerializer, \
    ShipmentSerializer


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [
        permissions.AllowAny
    ]


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    @action(methods=["get"], detail=True, serializer_class=ItemSerializer)
    def items(self, request, pk=None):
        shipment = self.get_object()
        items = shipment.items.all()
        serializer = self.get_serializer(items, many=True)
        return Response(serializer.data)
