from django.db import models

class Tipo(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    tipo = models.TextField(max_length=50, null=True)

class Fabricante(models.Model):
    id_fabricante = models.AutoField(primary_key=True)
    fabricante = models.TextField(max_length=50, null=True)

class Cor(models.Model):
    id_cor = models.AutoField(primary_key=True)
    cor = models.TextField(max_length=30, null=True)

class Tamanho(models.Model):
    id_tamanho = models.AutoField(primary_key=True)
    tamanho = models.IntegerField(null=True)