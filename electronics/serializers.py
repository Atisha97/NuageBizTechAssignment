from rest_framework import serializers

from .models import Electronics


class ElectronicsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    price = serializers.IntegerField()
    stock = serializers.IntegerField()

    def create(self, validated_data):
        return Electronics.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.stock = validated_data.get('stock', instance.stock)
        # instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance
