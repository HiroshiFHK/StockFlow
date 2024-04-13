from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# @login_required
def suppliers(request):
    return render(request, 'suppliers.html')