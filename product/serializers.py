from rest_framework import serializers

from .models import Item


class ItemSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=160)
    description = serializers.CharField(max_length=160)
    price = serializers.FloatField()

    class Meta:
        model = Item
        fields = [
            'id',
            'name',
            'description',
            'price'
        ]
