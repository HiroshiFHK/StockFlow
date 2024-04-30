from django.urls import path
from . import views

urlpatterns = [
    path('estoque/', views.stock, name="stock"),
    path('estoque/transaction/', views.transaction_create, name="transaction_create"),
]