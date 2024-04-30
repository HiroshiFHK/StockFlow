from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name="signin"),
    path('dashboard/', views.user_auth_login, name="signin_user"),
    path('register/', views.user_auth, name="register"),
    path('register/user/', views.user_auth_register, name="register_user")
]