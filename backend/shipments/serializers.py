from rest_framework import serializers

from .models import Country, City, Shipment


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = [
            'id',
            'name'
        ]
        read_only_fields = [
            'id'
        ]


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = [
            'id',
            'name',
            'country'
        ]
        read_only_fields = [
            'id'
        ]


class ShipmentSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(source='city.country',
                                                 read_only=True)
    full_address = serializers.CharField(source='get_full_address',
                                         read_only=True)

    class Meta:
        model = Shipment
        fields = [
            'id',
            'status',
            'country',
            'city',
            'address',
            'comment',
            'created_at',
            'updated_at',
            'sent_at',
            'full_address'
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
            'sent_at'
        ]
