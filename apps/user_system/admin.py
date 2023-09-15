from django.contrib import admin
from apps.user_system.models import Model_users


@admin.register(Model_users)
class UserAdmin (admin.ModelAdmin):
    list_display = ["email", "username", "creation","id"]
