import json

from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse

from app.internal.services.user_service import check_authorization, get_user


def get_info_about_user_via_id(request):
    t_id = request.GET["t_id"]
    reason, authorized = check_authorization(t_id)
    user_info = get_user(t_id)

    if user_info is None:
        return JsonResponse({"error": "zero matches for this id"})
    if authorized:
        resp = model_to_dict(user_info)
        return JsonResponse(resp)
    else:
        return JsonResponse({"error": "you need to set the phone first"})
