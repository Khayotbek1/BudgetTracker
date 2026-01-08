from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from .serializers import *

class IncomeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Income.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return IncomeSafeSerializer
        return IncomeCreateSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        user.balance += serializer.validated_data['amount']
        user.save()
        serializer.save(user=self.request.user)

