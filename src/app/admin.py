from django.contrib import admin

from app.internal.admin.admin_user import AdminUserAdmin
from app.internal.models.user import User

admin.site.site_title = "Backend course"
admin.site.site_header = "Backend course"
admin.site.register(User)