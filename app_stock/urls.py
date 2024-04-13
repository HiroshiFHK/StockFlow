from django.urls import path
from . import views

urlpatterns = [
    path('entries/', views.entries, name="entries"),
    path('exits/', views.exits, name="exits"),
]