from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import pandas as pd
import sqlite3

# @login_required
def user_dashboard(request):
    # Conecting to sqlite
    conection = sqlite3.connect('db.sqlite3')
    cursor = conection.cursor()

    # Data extraction for SQLITE
    cursor.execute('SELECT * FROM app_products_products')
    data = cursor.fetchall()

    # Data convertion
    df = pd.DataFrame(data, columns=['tipo', 'fabricante', 'genero', 'modelo', 'cor', 'tamanho', 'ncm', 'gtin', 'descricao','id_product', 'qtdproduto'])

    # Data analysis
    html_tabela = df.to_html(index = False)

    # Prepare for HTML
    context = {
        'tabela_html': html_tabela
    }

    return render(request, 'apps/app_dashboard/dashboard.html', context)