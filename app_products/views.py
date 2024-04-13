from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# @login_required
def user_products(request):
    return render(request, 'products.html')