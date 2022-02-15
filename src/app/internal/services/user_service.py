from app.internal.models.user import User


def create_user(first_name, last_name, username, t_id):
    obj, created = User.objects.get_or_create(
        first_name=first_name,
        last_name=last_name,
        username=username,
        id=t_id,
        defaults={'phone': ''}
    )
    return created


def save_phone_number(phone, t_id):
    obj, updated = User.objects.update_or_create(
        id=t_id,
        defaults={'phone': phone}
    )


def get_user(t_id):
    user = User.objects.get(id=t_id)
    return user


def check_authorization(t_id):
    try:
        user = User.objects.get(id=t_id)
    except Exception as e:
        return "Для начала нужно ввести команду /start", False
    else:
        if user.phone:
            return "", True
        else:
            return "Нужно ввести команду /set_phone!", False


