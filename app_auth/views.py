from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Products
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse

# FORMULÁRIO DE LOGIN
def user_login(request):
    if request.session.get('registration_data', {}):
        data = request.session.get('registration_data', {})
        del request.session['registration_data']
        return render(request, 'login.html', data)
    else:
        return render(request, 'login.html')
    
@require_POST # TODO FAZER VALIDAÇÕES E EXIBIR MENSAGENS
def user_auth_login(request):
    user = authenticate(email=request.POST['email'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('dashboard')
    else:
        return render(request, 'dashboard.html')

# PÁGINA DE CADASTRO DO USUÁRIO
def user_auth(request):
    return render(request, 'signup.html')

@require_POST
def user_auth_register(request):
    data = {}

    if request.POST['password'] != request.POST['confirm-password']:
        data["class"] = "alert"
        data['msg_title'] = 'Opss!!'
        data['msg'] = 'As senhas não coincidem!'

        return render(request, 'signup.html', data)
    
    try:
        if User.objects.get(username=request.POST['email']) or User.objects.get(email=request.POST['email']):
            data["class"] = "alert"
            data['msg_title'] = 'Opss!!'
            data['msg'] = 'Usuário já cadastrado no sistema!'

            return render(request, 'signup.html', data)
    
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
    
# Cadastro de produtos

def products(request):
    if request.method == 'POST':
        tipo = request.POST['tipo']
        fabricante = request.POST['fabricante']
        genero = request.POST['genero']
        modelo = request.POST['modelo']
        cor = request.POST['cor']
        tamanho = request.POST['tamanho']
        ncm = request.POST['ncm']
        gtin = request.POST['gtin']
        description = request.POST['description']
        novo_cadastro = Products (
            tipo = tipo,
            fabricante = fabricante,
            genero = genero,
            modelo = modelo,
            cor = cor,
            tamanho = tamanho,
            ncm = ncm,
            gtin = gtin,
            description = description
        )
        novo_cadastro.save()
        messages.success(request, 'O produto foi Cadastrado.')
        return redirect('products')
    else:
        messages.warning(request, 'Erro no cadastro do produto.')
        return render(request, 'products.html')
    
# Consulta de produtos

def queries(request):
    resultados = None
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        fabricante = request.POST.get('fabricante')
        genero = request.POST.get('genero')
        modelo = request.POST.get('modelo')
        cor = request.POST.get('cor')
        tamanho = request.POST.get('tamanho')
        ncm = request.POST.get('ncm')
        gtin = request.POST.get('gtin')
        description = request.POST.get('description')

        # Criando empty query
        query = Q()

        # Adicionar condições para a query baseado nos critérios
        if tipo:
            query &= Q(tipo=tipo)
        if fabricante:
            query &= Q(fabricante=fabricante)
        if genero:
            query &= Q(genero=genero)
        if modelo:
            query &= Q(modelo=modelo)
        if cor:
            query &= Q(cor=cor)
        if tamanho:
            query &= Q(tamanho=tamanho)
        if ncm:
            query &= Q(ncm=ncm)
        if gtin:
            query &= Q(gtin=gtin)

        # Execução da query
        resultados = Products.objects.filter(query)

    # Adicione os resultados
    context = {
        'resultados': resultados
    }

    return render(request, 'queries.html', {'resultados': resultados})

def entries(request):
    resultados = None
    if request.method == 'POST':
        gtin = request.POST.get('gtin')

        query = Q()

        if gtin:
            query &= Q(gtin=gtin)
        
        resultados = Products.objects.filter(query)

        if resultados.exists():
            resultado = resultados.first()
            novo_cadastro = Products(
                tipo = resultado.tipo,
                fabricante = resultado.fabricante,
                genero = resultado.genero,
                modelo = resultado.modelo,
                cor = resultado.cor,
                tamanho = resultado.tamanho,
                ncm = resultado.ncm,
                gtin = resultado.gtin,
                description = resultado.description
            )
            novo_cadastro.save()
            return JsonResponse({'success': 'O produto foi adicionado.'})
        else:
            return HttpResponse('O produto não existe.', status = 400)
        
    return render(request, 'entries.html')

def exits(request):
    resultados = None
    if request.method == 'POST':
        gtin = request.POST.get('gtin')

        query = Q()

        if gtin:
            query &= Q(gtin=gtin)
        
        resultados = Products.objects.filter(query)

        if resultados.exists():
            resultado = resultados.first()
            resultado.delete()
            return JsonResponse({'success': 'O produto foi removido.'})
        else:
            return HttpResponse('O produto não existe.', status = 400)

    return render(request, 'exits.html')