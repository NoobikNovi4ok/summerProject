from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "is_staff", "is_active"]
    search_fields = ["username", "email", "is_staff"]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
