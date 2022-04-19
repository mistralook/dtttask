from django.core.exceptions import ObjectDoesNotExist

from app.internal.models.user import User


def create_user(first_name, last_name, username, t_id):
    obj, created = User.objects.get_or_create(
        id=t_id, defaults={"phone": "", "first_name": first_name, "last_name": last_name, "username": username}
    )
    return created


def save_phone_number(phone, t_id):
    obj, updated = User.objects.update_or_create(id=t_id, defaults={"phone": phone})


def get_user(t_id):
    try:
        user = User.objects.get(id=t_id)
        return user
    except ObjectDoesNotExist:
        return None


def check_authorization(t_id):
    user = get_user(t_id)
    if user is None:
        return "Для начала нужно ввести команду /start", False
    else:
        if user.phone:
            return "", True
        else:
            return "Нужно ввести команду /set_phone!", False


def get_user_via_username(username):
    try:
        user = User.objects.get(username=username)
        return user
    except ObjectDoesNotExist:
        return None
