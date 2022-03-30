from django.contrib import admin

from app.internal.admin.account import AccountAdmin
from app.internal.admin.admin_user import AdminUserAdmin
from app.internal.admin.card import CardAdmin
from app.internal.admin.user import UserAdmin

admin.site.site_title = "Backend course"
admin.site.site_header = "Backend course"
