from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.Serializer):
    last_name = serializers.CharField(source="user.last_name", max_length=150)
    first_name = serializers.CharField(source="user.first_name", max_length=150)
    patronymic = serializers.CharField(max_length=150)
    email = serializers.EmailField(source="user.email", )
    phone_number = serializers.CharField(max_length=150, )
