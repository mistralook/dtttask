import json

from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse

from app.internal.services.user_service import get_user, check_authorization


def get_info_about_user_via_id(request):
    t_id = request.GET["t_id"]
    user_info = get_user(t_id)
    reason, authorized = check_authorization(t_id)
    resp = model_to_dict(user_info)
    if authorized:
        return JsonResponse(resp)
    elif not authorized:
        return JsonResponse({"error": "you need to set the phone first"})
    else:
        return JsonResponse({"error": "zero matches for this id"})
