from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    email = serializers.EmailField()
    contact = serializers.CharField(max_length=10)
    password = serializers.CharField(max_length=30)
    # author_id = serializers.IntegerField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.contact = validated_data.get('contact', instance.contact)
        # instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance
