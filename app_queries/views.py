from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# @login_required
def queries(request):
    return render(request, 'queries.html')