from django.urls import path
from .views import *

urlpatterns = [
    path('incomes/', IncomeListCreateAPIView.as_view())
]