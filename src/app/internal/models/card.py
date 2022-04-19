from django.db import models
from djmoney.models.fields import MoneyField

from .account import Account
from .user import User


class Card(models.Model):
    card_number = models.BigIntegerField(primary_key=True)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column="owner_id")
    balance = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.card_number}"
