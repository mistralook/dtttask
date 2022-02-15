import json

from django.http import JsonResponse, HttpResponse
from app.internal.services.user_service import get_user
from django.forms.models import model_to_dict


def get_info_about_user_via_id(request):
    t_id = request.GET['t_id']
    user_info = get_user(t_id)
    resp = model_to_dict(user_info)
    resp = ", ".join([f"{key}: {value}" for key, value in resp.items()])
    if user_info:
        return HttpResponse(f'{resp}')
    else:
        return JsonResponse({'error': 'zero matches for this id'})
