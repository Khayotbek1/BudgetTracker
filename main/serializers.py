from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from .models import Income, Expense
from users.serializers import ProfileSerializer


class IncomeSerializer(TranslatableModelSerializer):
    source = serializers.CharField(read_only=True)

    class Meta:
        model = Income
        fields = ("id", "amount", "source", "date", "created_at")


class IncomeCreateSerializer(TranslatableModelSerializer):
    translations = serializers.DictField(write_only=True)

    class Meta:
        model = Income
        fields = ("amount", "date", "translations")


class IncomeSafeSerializer(TranslatableModelSerializer):
    user = ProfileSerializer(read_only=True)
    source = serializers.CharField(read_only=True)

    class Meta:
        model = Income
        fields = "__all__"


class ExpenseSerializer(TranslatableModelSerializer):
    source = serializers.CharField(read_only=True)

    class Meta:
        model = Expense
        fields = ("id", "amount", "source", "date", "created_at")


class ExpenseCreateSerializer(TranslatableModelSerializer):
    translations = serializers.DictField(write_only=True)

    class Meta:
        model = Expense
        fields = ("amount", "date", "translations")
