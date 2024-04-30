from django.shortcuts import render
from app_products.models import Products
from .models import StockTransactions
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

# @login_required
def stock(request):
    produtos = Products.objects.all()
    for produto in produtos:
        produto.transacoes = StockTransactions.objects.filter(product=produto).order_by('-id_transaction')

    if request.session.get('transaction_data', {}):
        data = request.session.get('transaction_data', {})
        del request.session['transaction_data']

        return render(request, 'apps/app_stock/stock.html', {'produtos': produtos, **data})
    else:
        return render(request, 'apps/app_stock/stock.html', {'produtos': produtos})


def transaction_create(request):
    data = {}

    if request.method == 'POST':
        gtin = request.POST.get('gtin')
        quantity = int(request.POST.get('qtd'))
        transaction_type = request.POST.get('transaction')

        try:
            produto_existente = Products.objects.get(gtin=gtin)
        except Products.DoesNotExist:
            data = {
                'msg_title': 'Ops!',
                'msg': 'Produto não encontrado!',
                'class': 'alert'
            }
            
            request.session['transaction_data'] = data

            return HttpResponseRedirect(reverse('stock'))

        if transaction_type == 'entrada':
            produto_existente.qtdproduto += quantity
        elif transaction_type == 'saida':
            if produto_existente.qtdproduto < quantity:
                data = {
                    'msg_title': 'Ops!',
                    'msg': 'Quantidade insuficiente no estoque!',
                    'class': 'alert'
                }
                
                request.session['transaction_data'] = data

                return HttpResponseRedirect(reverse('stock'))
            
            produto_existente.qtdproduto -= quantity

        produto_existente.save()

        transacao = StockTransactions(
            product=produto_existente,
            transaction_type=transaction_type,
            quantity=quantity,
            transaction_date=timezone.now()
        )
        transacao.save()

        data = {
            'msg_title': '',
            'msg': 'Atualização efetuada com sucesso!',
            'class': 'success'
        }
        
        request.session['transaction_data'] = data

        return HttpResponseRedirect(reverse('stock'))

    return render(request, 'apps/app_stock/stock.html')
