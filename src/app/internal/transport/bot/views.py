import json

from django.http import JsonResponse
from django.views import View
from telegram import Update

from app.internal.bot import TBot


class BotWebHookView(View):
    def webhook_handler(self, request):
        bot = TBot()
        body = json.loads(request.body)
        update = Update.de_json(body, bot)
        bot.webhook(update)
        return JsonResponse({"Ok": "request processed"})