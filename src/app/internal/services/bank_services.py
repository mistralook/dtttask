import decimal

from app.internal.models.card import Card
from app.internal.models.user import User
from django.core.exceptions import ObjectDoesNotExist

from django.db import transaction

from .user_service import get_user, get_user_via_username


@transaction.atomic
def transfer_operation(from_card, to_card, amount):
    if from_card.balance <= 0:
        return "Negative balance. You can't send money from this card."
    from_card.balance -= decimal.Decimal(amount)
    to_card.balance += decimal.Decimal(amount)
    from_card.save()
    to_card.save()
    return f"The operation was successful. \n" \
           f"From: {from_card.card_number} ({from_card.owner_id}) \n" \
           f"To: {to_card.card_number} ({to_card.owner_id}) \n" \
           f"{amount} were sent"


def get_card_by_card_number(card_number):
    try:
        card = Card.objects.get(card_number=card_number)
        return card
    except ObjectDoesNotExist:
        return None


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
    source_card = int(source)
    source_card = get_card_by_card_number(source_card)
    if source_card is None:
        return "Invalid source. Card does not exist"
    try:
        destination = int(destination)  # card
        receiver_card = get_card_by_card_number(destination)
        if receiver_card is None:
            return "Invalid receiver. Card does not exist"
        operation = transfer_operation(source_card, receiver_card, amount)
    except ValueError:  # login
        if "@" in destination:
            destination = destination[1:]
        user_id = get_user_via_username(destination)
        if user_id is None:
            return "Invalid receiver. User does not exist."
        receiver_card = Card.objects.filter(owner_id=user_id).first()
        if receiver_card is None:
            return "Invalid receiver. User does not have cards."
        operation = transfer_operation(source_card, receiver_card, amount)
    return f"{operation}"
