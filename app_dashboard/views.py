import plotly.express as px
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
    
    # Extract data from SQLITE
    data = pd.read_sql_query('SELECT * FROM app_products_products', connection)

    # Analyze data
    # Chart 1: Produtos x Fabricante
    fig1 = px.bar(data, x='fabricante', y='qtdproduto', title='Produtos x Fabricante', labels={'fabricante': 'Fabricante', 'qtdproduto': 'Quantidade de Produtos'}, text=data['qtdproduto'])

    # Chart 2: Produtos x Gênero
    fig2 = px.pie(data, names='genero', values='qtdproduto', title='Produtos x Gênero', category_orders={'genero': ['Y', 'X', 'Z']})
    fig2.update_traces(textinfo='label+percent', texttemplate='%{value} (%{percent})')

    # Convert figures to HTML
    div1 = fig1.to_html(full_html=False)
    div2 = fig2.to_html(full_html=False)

    # Close connection
    connection.close()

    # Prepare context for HTML
    context = {
        'div_grafico1': div1,
        'div_grafico2': div2,
    }

    return render(request, 'apps/app_dashboard/dashboard.html', context)