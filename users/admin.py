from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from users.models import userProfile

class UserProfileInline(admin.StackedInline):
    model = userProfile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_life_stage', 'get_state', 'is_staff')
    
    def get_life_stage(self, obj):
        try:
            return obj.userprofile.get_life_stage_display()
        except userProfile.DoesNotExist:
            return '-'
    get_life_stage.short_description = 'Life Stage'

    def get_state(self, obj):
        try:
            return obj.userprofile.state
        except userProfile.DoesNotExist:
            return '-'
    get_state.short_description = 'State'

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register userProfile separately for direct management
@admin.register(userProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'cast', 'state', 'profession', 'education_level', 'life_stage', 'preferred_language')
    list_filter = ('life_stage', 'education_level', 'preferred_language', 'state')
    search_fields = ('user__username', 'user__email', 'cast', 'state', 'profession')
