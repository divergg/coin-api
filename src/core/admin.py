from django.contrib import admin
from src.core.models import User, ScheduledReward



class SuperUserPermissionsMixin:

    def has_delete_permission(self, request, obj=None):
        """Allow deletion only for superusers."""
        return request.user.is_superuser

    def has_add_permission(self, request):
        """Allow adding only for superusers."""
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        """Allow changing only for superusers."""
        return request.user.is_superuser



class ScheduledRewardInline(admin.TabularInline):
    model = ScheduledReward
    extra = 1
    fields = ('execute_at', 'amount')

@admin.register(User)
class UserAdmin(SuperUserPermissionsMixin, admin.ModelAdmin):
    """Custom admin for User model."""

    inlines = (ScheduledRewardInline,)

    list_display = (
        'id',
        'username',
        'email',
        'coins'
    )
    readonly_fields = ('username', 'email')
    search_fields = ('username', 'email')
