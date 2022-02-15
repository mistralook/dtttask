# from django.conf import settings
from app.internal.transport.bot.handlers import start_command, set_phone, phone_num_handler, me, error
from config.settings import API_TOKEN
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters


def start():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('set_phone', set_phone)],
        states={
            1: [MessageHandler(Filters.text, phone_num_handler, pass_user_data=True)]
        },
        fallbacks=[]
    )
    dp.add_handler(conversation_handler)
    dp.add_handler(CommandHandler("me", me))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
