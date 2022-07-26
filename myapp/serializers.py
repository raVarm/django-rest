from rest_framework import serializers
from .models import User_service

class User_service_serializer(serializers.Serializer):
    name = serializers.CharField(max_length=70)
    service = serializers.CharField(max_length=120)
    service_man = serializers.CharField(max_length=70)
    date = serializers.DateField()
    check_in = serializers.TimeField()
    check_out = serializers.TimeField()
    cost = serializers.IntegerField()

    def create(self, validated_data):
        return User_service.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.service = validated_data.get('service', instance.service)
        instance.service_man = validated_data.get('service_man', instance.service_man)
        instance.date = validated_data.get('date', instance.date)
        instance.check_in = validated_data.get('check_in', instance.check_in)
        instance.check_out = validated_data.get('check_out', instance.check_out)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.save()
        return instance