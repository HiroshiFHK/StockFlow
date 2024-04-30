from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# @login_required
def user_settings(request):
    return render(request, 'apps/app_settings/settings.html')