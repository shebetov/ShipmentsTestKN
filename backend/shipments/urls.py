from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CountryViewSet, CityViewSet, ShipmentViewSet


router = DefaultRouter()
router.register(r'countries', CountryViewSet, basename="country")
router.register(r'cities', CityViewSet, basename="city")
router.register(r'shipments', ShipmentViewSet, basename="shipment")

urlpatterns = [
    path('', include(router.urls)),
]
