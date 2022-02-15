from django.urls import path
from app.internal.transport.rest.handlers import get_info_about_user_via_id

urlpatterns = [
    path('me', get_info_about_user_via_id)
]
