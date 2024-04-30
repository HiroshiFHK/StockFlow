from django.db import models
from app_products.models import Products
from django.utils import timezone

class StockTransactions(models.Model):
    id_transaction = models.AutoField(primary_key=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=[('entrada', 'Entrada'), ('saida', 'Saída')])
    quantity = models.IntegerField(null=False)
    transaction_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.product} - {self.transaction_type} - {self.quantity} - {self.transaction_date}"