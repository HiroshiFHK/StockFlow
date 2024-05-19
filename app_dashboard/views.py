import matplotlib
matplotlib.use('Agg')  # Use o backend 'Agg' para evitar problemas com interfaces gráficas
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import io
import base64

# @login_required
def user_dashboard(request):
    # Conectando ao sqlite
    conection = sqlite3.connect('db.sqlite3')
    cursor = conection.cursor()

    # Extração de dados do SQLITE
    cursor.execute('SELECT * FROM app_products_products')
    data = cursor.fetchall()

    # Conversão de dados
    df = pd.DataFrame(data, columns=['tipo', 'fabricante', 'genero', 'modelo', 'cor', 'tamanho', 'ncm', 'gtin', 'descricao','id_product', 'qtdproduto'])

    # Análise de dados
    # html_tabela = df.to_html(index=False)
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
    plt.title("Gráfico: Nº de Produtos x Fabricante")

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    # Preparar para o HTML
    context = {
        # 'tabela_html': html_tabela,
        'imagem_grafico': f"data:image/png;base64,{image_base64}"
    }

    return render(request, 'apps/app_dashboard/dashboard.html', context)
