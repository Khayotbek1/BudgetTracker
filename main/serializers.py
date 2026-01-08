from rest_framework import serializers
from .models import *
from users.serializers import ProfileSerializer


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

class IncomeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ('id', 'amount', 'source', 'date', 'created_at')



class IncomeSafeSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)
    class Meta:
        model = Income
        fields = '__all__'