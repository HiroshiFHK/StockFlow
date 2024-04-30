from django.db import models

class Products(models.Model):
    id_product = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, null=False)
    fabricante = models.CharField(max_length=50, null=False)
    genero = models.CharField(max_length=10, null=False)
    modelo = models.CharField(max_length=50, null=False)
    cor = models.CharField(max_length=50, null=False)
    tamanho = models.IntegerField(null=False)
    descricao = models.TextField(null=False)
    ncm = models.CharField(max_length=50, null=False)
    gtin = models.BigIntegerField(null=False)
    qtdproduto = models.IntegerField(null=False, default=0)
