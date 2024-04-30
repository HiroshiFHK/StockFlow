from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.urls import reverse

# FORMULÁRIO DE LOGIN
def user_login(request):
    if request.session.get('registration_data', {}):
        data = request.session.get('registration_data', {})
        del request.session['registration_data']
        return render(request, 'apps/app_auth/login.html', data)
    else:
        return render(request, 'apps/app_auth/login.html')
    
@require_POST # TODO FAZER VALIDAÇÕES E EXIBIR MENSAGENS
def user_auth_login(request):
    user = authenticate(email=request.POST['email'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('dashboard')
    else:
        return render(request, 'apps/app_dashboard/dashboard.html')

# PÁGINA DE CADASTRO DO USUÁRIO
def user_auth(request):
    return render(request, 'apps/app_auth/signup.html')

@require_POST
def user_auth_register(request):
    data = {}

    if request.POST['password'] != request.POST['confirm-password']:
        data["class"] = "alert"
        data['msg_title'] = 'Opss!!'
        data['msg'] = 'As senhas não coincidem!'

        return render(request, 'apps/app_auth/signup.html', data)
    
    try:
        if User.objects.get(username=request.POST['email']) or User.objects.get(email=request.POST['email']):
            data["class"] = "alert"
            data['msg_title'] = 'Opss!!'
            data['msg'] = 'Usuário já cadastrado no sistema!'

            return render(request, 'apps/app_auth/signup.html', data)
    
    except User.DoesNotExist:
        username = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.first_name = first_name
        new_user.last_name = last_name

        new_user.save()

        data['msg_title'] = 'Wow!!'
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data["class"] = "success"
        
        request.session['registration_data'] = data

        return HttpResponseRedirect(reverse('signin'))
