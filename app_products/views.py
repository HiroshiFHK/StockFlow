# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from app_products.models import Products
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib.sessions.backends.db import SessionStore

# @login_required
def user_products(request):
    if request.session.get('product_data', {}):
        data = request.session.get('product_data', {})
        del request.session['product_data']
        return render(request, 'apps/app_products/products.html', data)
    else:
        return render(request, 'apps/app_products/products.html')

@require_POST
def cad_products(request):
    data = {}

    gtin = request.POST['gtin']

    if Products.objects.filter(gtin=gtin).exists():
        data['msg_title'] = 'Opss!!'
        data["class"] = "alert"
        data['msg'] = 'O GTIN já está cadastrado!'

        request.session['product_data'] = data

        return HttpResponseRedirect(reverse('products'))

    if request.method == 'POST':
        tipo = request.POST['tipo']
        fabricante = request.POST['fabricante']
        genero = request.POST['genero']
        modelo = request.POST['modelo']
        cor = request.POST['cor']
        tamanho = request.POST['tamanho']
        descricao = request.POST['descricao']
        gtin = request.POST['gtin']
        ncm = request.POST['ncmDropdown']
        qtdproduto = request.POST['qtdProducts']
        
        produto = Products.objects.create (
            tipo = tipo,
            fabricante = fabricante,
            genero = genero,
            modelo = modelo,
            cor = cor,
            tamanho = tamanho,
            ncm = ncm,
            gtin = gtin,
            descricao = descricao,
            qtdproduto = qtdproduto
        )

        produto.save()

        data['msg_title'] = ''
        data['msg'] = 'Produto cadastrado com sucesso!'
        data["class"] = "success"
        
        request.session['product_data'] = data

        return HttpResponseRedirect(reverse('products'))
    else:
        data['msg_title'] = 'Opss!!'
        data["class"] = "alert"
        data['msg'] = 'Algo deu errado!'

        return render(request, 'apps/app_products/products.html')

def delete_products(request, id_product):
    produto = Products.objects.filter(pk=id_product)
    produto.delete()
    return HttpResponseRedirect(reverse('queries'))

def update_products(request, id_product):
    produtos = Products.objects.filter(pk=id_product)
    return render(request, 'apps/app_products/update.html', {'produtos': produtos})
    