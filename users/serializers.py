from rest_framework import serializers
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'balance')
        extra_kwargs = {
            'password': {'write_only': True},
            'balance': {'required': False},
        }
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'balance', 'date_joined')
        extra_kwargs = {
            'balance':{'read_only': True},
        }
