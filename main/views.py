from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from .serializers import *

class IncomeListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['translations__source']
    ordering_fields = ['amount', 'date', 'created_at']
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return IncomeSafeSerializer
        return IncomeCreateSerializer

    def perform_create(self, serializer):
        user = self.request.user
        amount = serializer.validated_data['amount']
        user.balance += amount
        user.save()
        serializer.save(user=user)



class ExpenseListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=['api'],
        operation_description='Get Expense list',
        manual_parameters=[
            openapi.Parameter(
                name='search',
                in_=openapi.IN_QUERY,
                description='Search by source',
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                name='ordering',
                in_=openapi.IN_QUERY,
                description='Ordering by amount, created_at, date',
                type=openapi.TYPE_STRING,
                enum=['created_at', '-created_at', 'amount', '-amount', 'date', '-date'],
            )
        ],
    )
    def get(self,request):
        expenses = Expense.objects.filter(user=request.user)

        search = request.GET.get('search')
        if search is not None:
            expenses = expenses.filter(source__icontains=search)
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

        ordering = Expense.objects.GET.get('ordering')
        if ordering is not None:
            expenses = expenses.order_by(ordering)
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        tags=['api'],
        request_body=ExpenseSerializer,
    )
    def post(self,request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                user=self.request.user
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

