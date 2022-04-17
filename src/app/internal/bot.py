# from django.conf import settings
from queue import Queue

from telegram import Bot
from telegram.ext import CommandHandler, ConversationHandler, Filters, MessageHandler, Dispatcher, Updater

from app.internal.transport.bot.bank_handlers import balance_by_account, balance_by_card
from app.internal.transport.bot.handlers import error, me, phone_num_handler, set_phone, start_command
from config.settings import API_TOKEN

class TBot:
    def __init__(self):
        # self.bot = Bot(API_TOKEN)
        # self.update_queue = Queue()
        # self.dp = Dispatcher(self.bot, update_queue=Queue())
        self.updater = Updater(API_TOKEN, use_context=True)
        self.dp = self.updater.dispatcher
        self.start()

    def start(self):
        self.dp.add_handler(CommandHandler("start", start_command))
        conversation_handler = ConversationHandler(
            entry_points=[CommandHandler("set_phone", set_phone)],
            states={1: [MessageHandler(Filters.text, phone_num_handler, pass_user_data=True)]},
            fallbacks=[],
        )
        self.dp.add_handler(conversation_handler)
        self.dp.add_handler(CommandHandler("me", me))
        self.dp.add_handler(CommandHandler("balance_by_card", balance_by_card))
        self.dp.add_handler(CommandHandler("balance_by_account", balance_by_account))
        self.dp.add_error_handler(error)

    # def set_webhook(self):
    #     self.bot.setWebhook(url="triplehover.backend22.2tapp.cc")

    def poll(self, update):
        # self.dp.process_update(update)
        self.updater.start_polling()
        self.updater.idle()

# def start():
#     updater = Updater(API_TOKEN, use_context=True)
#     dp = updater.dispatcher
#
#     dp.add_handler(CommandHandler("start", start_command))
#     conversation_handler = ConversationHandler(
#         entry_points=[CommandHandler("set_phone", set_phone)],
#         states={1: [MessageHandler(Filters.text, phone_num_handler, pass_user_data=True)]},
#         fallbacks=[],
#     )
#     dp.add_handler(conversation_handler)
#     dp.add_handler(CommandHandler("me", me))
#     dp.add_handler(CommandHandler("balance_by_card", balance_by_card))
#     dp.add_handler(CommandHandler("balance_by_account", balance_by_account))
#     dp.add_error_handler(error)



