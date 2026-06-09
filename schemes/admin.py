from django.contrib import admin
from .models import Schemes, Notification

@admin.register(Schemes)
class SchemesAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'scheme_type', 'state', 'caste', 'age_limit', 'income_limit', 'deadline')
    list_filter = ('scheme_type', 'state', 'caste', 'profession')
    search_fields = ('title_en', 'title_hi', 'title_mr', 'description_en', 'state', 'caste')
    ordering = ('-date_created',)
    filter_horizontal = ('required_documents',)
    fieldsets = (
        ('Basic Info (English)', {
            'fields': ('title_en', 'description_en')
        }),
        ('Hindi Localization', {
            'fields': ('title_hi', 'description_hi'),
            'classes': ('collapse',),
        }),
        ('Marathi Localization', {
            'fields': ('title_mr', 'description_mr'),
            'classes': ('collapse',),
        }),
        ('Timeline & Dates', {
            'fields': ('scheme_application_start_date', 'deadline_scheme_application', 'deadline')
        }),
        ('Eligibility Filters', {
            'fields': ('age_limit', 'income_limit', 'caste', 'state', 'profession', 'category', 'scheme_type')
        }),
        ('Requirements', {
            'fields': ('required_documents',)
        }),
    )

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'scheme', 'type', 'is_read', 'created_at')
    list_filter = ('type', 'is_read', 'created_at')
    search_fields = ('user__username', 'scheme__title_en', 'message')
    ordering = ('-created_at',)
