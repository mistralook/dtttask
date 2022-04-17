from django.core.management.base import BaseCommand

from app.internal.bot import TBot


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot = TBot()
        # bot.set_webhook()
        bot.poll()
