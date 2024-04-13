from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.user_clients, name="clients"),
]