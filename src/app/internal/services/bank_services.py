from app.internal.models.card import Card

from .user_service import get_user


def get_balance_by_card(t_id, card_number):
    try:
        balance = Card.objects.get(id=t_id, card_number=card_number).balance
    except Exception:
        return None
    return balance


def get_balance_by_account(t_id, account_number):
    user = get_user(t_id).id
    try:
        cards = Card.objects.filter(id=user, account=account_number)
    except Exception:
        return None
    balance = sum([card.balance for card in cards])
    return balance
