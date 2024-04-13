from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# @login_required
def entries(request):
    return render(request, 'entries.html')

# @login_required
def exits(request):
    return render(request, 'exits.html')