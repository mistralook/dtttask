from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt

from config.settings import API_TOKEN
from app.internal.transport.bot.views import BotWebHookView

urlpatterns = [
          path("admin/", admin.site.urls),
          path("api/", include("app.internal.urls")),
          path(f"{API_TOKEN}", csrf_exempt(BotWebHookView.as_view()))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
