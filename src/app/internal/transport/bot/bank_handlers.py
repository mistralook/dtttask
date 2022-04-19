import re

from app.internal.services.bank_services import get_balance_by_account, get_balance_by_card, transfer_money_to_card


def get_balance(t_id, subject, subject_number, balance_method):
    balance = balance_method(t_id, subject_number)
    if balance is None:
        return f"{subject} not found"
    return f"{balance}"


def check_balance_card(t_id, card_number):
    if len(card_number) != 16 or re.match(r"\d{16}", card_number) is None:
        return "Please, write card number in format xxxx-yyyy-zzzz-wwww or xxxxyyyyzzzzwwww"
    balance = get_balance(t_id, "card", card_number, get_balance_by_card)
    return balance


def validate_amount(amount):
    try:
        amount = int(amount)
        if amount < 0:
            return "amount must be a positive number."
        elif amount == 0:
            return "amount must be bigger than zero"
    except ValueError:
        return "amount must be a positive number."
    return amount


def balance_by_card(update, context):
    t_id = update.message.from_user.id
    args = context.args
    if not args:
        return update.message.reply_text(
            "To get balance via card number, you need to write it after. F.e. /balance_by_card 1234546789012345"
        )
    if len(args) == 1:
        card_number = args[0]
        card_number = card_number.replace("-", "")
        answer = check_balance_card(t_id, card_number)
        update.message.reply_text(answer)

    elif len(args) == 4:
        card_number = "".join(nums for nums in args)
        answer = check_balance_card(t_id, card_number)
        update.message.reply_text(answer)


def balance_by_account(update, context):
    t_id = update.message.from_user.id
    args = context.args
    if not args:
        return update.message.reply_text(
            "To get balance via account number, you need to write it after. F.e. /balance_by_account 1234..."
        )
    account_number = args[0]
    balance = get_balance(t_id, "account", account_number, get_balance_by_account)
    update.message.reply_text(balance)


def transfer_money(update, context):
    t_id = update.message.from_user.id
    args = context.args
    if not args:
        return update.message.reply_text(
            "To transfer money, use this template:\n "
            "/transfer_money (from_card_number) (to_card_number|to_telegram_login) (amount_of_money).\n "
            "F.e. /transfer_money 1111-2222-3333-4444 @Durov 1337"
        )
    if len(args) == 3:
        sender_card = args[0].replace("-", "")
        destination = args[1].replace("-", "")
        if sender_card == destination:
            "Invalid operation. You can't send money to yourself."
        amount = validate_amount(args[2])
        if type(amount) is str:
            return update.message.reply_text(f"Invalid amount. Reason: {amount}")
        answer = transfer_money_to_card(sender_card, destination, amount)
        update.message.reply_text(answer)
    else:
        return update.message.reply_text(
            "Invalid command. Type '/transfer_money' to see the template."
        )
