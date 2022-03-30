# from django.conf import settings
from telegram.ext import CommandHandler, ConversationHandler, Filters, MessageHandler, Updater

from app.internal.transport.bot.handlers import error, me, phone_num_handler, set_phone, start_command
from app.internal.transport.bot.bank_handlers import balance_by_card, balance_by_account
from config.settings import API_TOKEN


def start():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler("set_phone", set_phone)],
        states={1: [MessageHandler(Filters.text, phone_num_handler, pass_user_data=True)]},
        fallbacks=[],
    )
    dp.add_handler(conversation_handler)
    dp.add_handler(CommandHandler("me", me))
    dp.add_handler(CommandHandler("balance_by_card", balance_by_card))
    dp.add_handler(CommandHandler("balance_by_account", balance_by_account))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
