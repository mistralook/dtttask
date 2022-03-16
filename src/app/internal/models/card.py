from django.db import models
from djmoney.models.fields import MoneyField
from .account import Account
from .user import User


class Card(models.Model):
    card_number = models.BigIntegerField(primary_key=True)
    id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    balance = MoneyField(max_digits=14, decimal_places=2, null=True, default_currency=None)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.card_number}"
