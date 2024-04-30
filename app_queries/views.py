from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from app_products.models import Products

def queries(request):
    produtos = Products.objects.all()
    return render(request, 'apps/app_queries/queries.html', {'produtos':produtos})