import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for headless environments
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# @login_required (optional)  # Add decorator if needed
def user_dashboard(request):
    # Connect to sqlite
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()

    # Extract data from SQLITE
    cursor.execute('SELECT * FROM app_products_products')
    data = cursor.fetchall()

    # Convert data to DataFrame
    df = pd.DataFrame(data, columns=['tipo', 'fabricante', 'genero', 'modelo', 'cor', 'tamanho', 'ncm', 'gtin', 'descricao', 'id_product', 'qtdproduto'])

    # Analyze data
    # Create separate figures for each chart to avoid conflicts
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()

    # Chart 1: Produtos x Fabricante
    prod_fab = """
        SELECT
            fabricante,
            SUM(qtdproduto) AS soma_prod
        FROM
            app_products_products app
        GROUP BY
            fabricante
    """
    dados_fab = pd.read_sql(prod_fab, connection)
    ax1.bar(dados_fab.fabricante, dados_fab.soma_prod, color='lightgreen')
    ax1.set_title("Produtos x Fabricante")

    # Chart 2: Produtos x Gênero
    prod_gen = """
        SELECT
            genero,
            SUM(qtdproduto) AS soma_prod
        FROM
            app_products_products app
        GROUP BY
            genero
    """
    dados_gen = pd.read_sql(prod_gen, connection)
    ax2.barh(dados_gen.genero, dados_gen.soma_prod, color='skyblue')
    ax2.set_title("Produtos x Gênero")

    # Save figures to BytesIO objects
    buf1 = BytesIO()
    fig1.savefig(buf1, format='png')
    buf1.seek(0)
    image_base64_1 = base64.b64encode(buf1.read()).decode('utf-8')
    buf1.close()

    buf2 = BytesIO()
    fig2.savefig(buf2, format='png')
    buf2.seek(0)
    image_base64_2 = base64.b64encode(buf2.read()).decode('utf-8')
    buf2.close()

    # Close connection
    connection.close()

    # Prepare context for HTML
    context = {
        'imagem_grafico1': f"data:image/png;base64,{image_base64_1}",
        'imagem_grafico2': f"data:image/png;base64,{image_base64_2}",
    }

    return render(request, 'apps/app_dashboard/dashboard.html', context)
