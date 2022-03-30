from django.contrib import admin

from app.internal.models.account import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass
