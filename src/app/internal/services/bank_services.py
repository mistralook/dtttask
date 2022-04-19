from app.internal.models.card import Card

from .user_service import get_user, get_user_via_username


def get_balance_by_card(t_id, card_number):
    try:
        balance = Card.objects.get(owner_id=t_id, card_number=card_number).balance
    except Exception:
        return None
    return balance


def get_balance_by_account(t_id, account_number):
    user = get_user(t_id).id
    try:
        cards = Card.objects.filter(owner_id=user, account=account_number)
    except Exception:
        return None
    balance = sum([card.balance for card in cards])
    return balance

def transfer_money_to_card(source, destination, amount):
    try:
        destination = int(destination) # card
        # card = Card.objects.get(card_number=destination).balance
        # user = get_user_via_username()
        # return card
    except ValueError: # login
        if "@" in destination:
            destination = destination[1:]
        receiver_card = Card.objects.get(owner_id=destination).balance
        return receiver_card
    return f"{destination}, {type(destination)}"
