from rest_framework import serializers
from .models import FuelPrice

class FuelPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelPrice
        fields = ('city', 'price')
        

class RouteSerializer(serializers.Serializer):
    start = serializers.CharField(max_length=255)
    end = serializers.CharField(max_length=255)