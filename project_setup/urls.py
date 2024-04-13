from django.urls import path, include

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),

    # DASHBOARD
    path('dashboard/', include('app_dashboard.urls')),
    path('dashboard/', include('app_clients.urls')),
    path('dashboard/', include('app_products.urls')),
    path('dashboard/', include('app_settings.urls')),
    path('dashboard/', include('app_stock.urls')),
    path('dashboard/', include('app_stock.urls')),
    path('dashboard/', include('app_queries.urls')),
    path('dashboard/', include('app_suppliers.urls')),

    path("", include('app_auth.urls')),
    
]