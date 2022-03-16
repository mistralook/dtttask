import re

from app.internal.services.bank_services import get_balance_by_card, get_balance_by_account


def balance_by_card(update, context):
    t_id = update.message.from_user.id
    args = context.args
    if args:
        card_number = args[0]
        if len(card_number) != 16 or re.match(r"\d{16}", card_number) is None:
            return update.message.reply_text(f"Please, write card number in format xxxxyyyyzzzzwwww")
        balance = get_balance_by_card(t_id, card_number)
        if balance is None:
            return update.message.reply_text(f"Card not found")
        return update.message.reply_text(f"{balance}")
    return update.message.reply_text(
        f"To get balance via card number, you need to write it after. F.e. "
        f"/balance_by_card 1234546789012345")


def balance_by_account(update, context):
    t_id = update.message.from_user.id
    args = context.args
    if args:
        account_number = args[0]
        balance = get_balance_by_account(t_id, account_number)
        if balance is None:
            return update.message.reply_text(f"Account not found")
        return update.message.reply_text(f"{balance}")
    return update.message.reply_text(
        f"To get balance via account number, you need to write it after. "
        f"F.e. /balance_by_account 1234...")
