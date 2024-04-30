from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.user_products, name="products"),
    path('products/create/', views.cad_products, name="cad_products"),
    path('products/update/<int:id_product>', views.update_products, name='update_products'),
    path('products/delete/<int:id_product>', views.delete_products, name='delete_products'),
]