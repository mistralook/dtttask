import re

from telegram.ext import ConversationHandler

from app.internal.services.user_service import check_authorization, create_user, get_user, save_phone_number, \
    show_user_favourites


def start_command(update, context):
    user_info = update.message.from_user
    t_id = user_info.id
    first_name = user_info.first_name
    last_name = user_info.last_name
    username = user_info.username
    was_created = create_user(first_name, last_name, username, t_id)
    if was_created is True:
        update.message.reply_text(f"Пользователь был сохранен, {first_name}!")
    else:
        update.message.reply_text("Такой пользователь уже был создан!")


def set_phone(update, context):
    update.message.reply_text('Пожалуйста, введите номер телефон в формате "+7..."')
    return 1


def phone_num_handler(update, context):
    phone_number = str(update.message.text)
    if len(phone_number) != 12 or re.match(r"^(\+7+([0-9]){10})", phone_number) is None:
        update.message.reply_text("Номер введен неверно :( Попробуйте заново!")
        return ConversationHandler.END
    else:
        t_id = update.message.from_user.id
        save_phone_number(phone_number, t_id)
        update.message.reply_text("Номер был добавлен!")
        return ConversationHandler.END


def me(update, context):
    t_id = update.message.from_user.id
    reason, authorized = check_authorization(t_id)
    if authorized:
        user_info = get_user(t_id)
        full_name = f'{user_info.first_name} {user_info.last_name if user_info.last_name is not None else ""}'

        update.message.reply_text(
            f"""Информация о текущем пользователе
Имя: {full_name}
Имя пользователя: {user_info.username}
Номер телефона: {user_info.phone}
        """
        )
    else:
        update.message.reply_text(reason)


def show_favourites(update, context):
    t_id = update.message.from_user.id
    reason, authorized = check_authorization(t_id)
    if authorized:
        answer = show_user_favourites(t_id)
        update.message.reply_text(answer)
    else:
        update.message.reply_text(reason)


def error(update, context):
    print(f"Oopsie! Something is wrong: {context.error}")
