from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from PIL import Image 
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

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
    sql = """
        select
            max(fabricante) fabricantes,
            sum(qtdproduto) soma_prod
        from
            app_products_products app
        group by
            fabricante
            """
    dados = pd.read_sql(sql, conection)
    plt.bar(dados.fabricantes, dados.soma_prod)
    plt.title("Gráfico de Colunas por Fabricantes")
    caminho_arq = settings.BASE_DIR/ 'templates' / 'static'/'colunas.png'
    print(caminho_arq)
    plt.savefig(caminho_arq)

    # Prepare for HTML
    context = {
        'tabela_html': html_tabela,
        'imagem_grafico': 'caminho_arq'
    }

    return render(request, 'apps/app_dashboard/dashboard.html', context)