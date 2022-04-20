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


def show_user_favourites(t_id):
    user = get_user(t_id)
    return f"Your favourites:\n" \
           f"{list(user.favourites.all().values_list())}"


def add_to_user_favourites(t_id, user_to_add):
    user = get_user(t_id)
    if "@" in user_to_add:
        user_to_add = user_to_add[1:]
    featured_user = get_user_via_username(user_to_add)
    if featured_user is None:
        return "Invalid operation. The user to add does not exist"
    user.favourites.add(featured_user)
    user.save()
    return f"{featured_user.username} was successfully added to your favourites list"


def remove_from_user_favourites(t_id, user_to_remove):
    user = get_user(t_id)
    if "@" in user_to_remove:
        user_to_remove = user_to_remove[1:]
    featured_user_to_remove = get_user_via_username(user_to_remove) # ремувать только тех, которые есть в favourites
    if featured_user_to_remove is None:
        return "Invalid operation. The user to remove does not exist"
    user.favourites.remove(featured_user_to_remove)
    user.save()
    return f"{featured_user_to_remove.username} was successfully removed from your favourites list"

