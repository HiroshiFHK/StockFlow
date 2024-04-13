from django.db import models

class Products(models.Model):
    id_products = models.AutoField(primary_key = True)
    tipo = models.TextField(max_length = 255)
    fabricante = models.TextField(max_length = 255)
    genero = models.TextField(max_length = 255)
    modelo = models.TextField(max_length = 255)
    cor = models.TextField(max_length = 255)
    tamanho = models.IntegerField()
    description = models.TextField(max_length = 255, null = True)
    ncm = models.IntegerField()
    gtin = models.BigIntegerField()