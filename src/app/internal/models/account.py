from django.db import models
from .user import User


class Account(models.Model):
    account_number = models.BigIntegerField(primary_key=True)
    account_holder = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.account_number}"
