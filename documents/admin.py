from django.contrib import admin
from .models import Documents, ServiceCenter

@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'category', 'issuing_authority', 'state', 'caste', 'required_for_application', 'date_created')
    list_filter = ('category', 'required_for_application', 'state', 'caste')
    search_fields = ('title_en', 'title_hi', 'title_mr', 'description_en', 'issuing_authority')
    ordering = ('-date_created',)
    fieldsets = (
        ('Basic Info (English)', {
            'fields': ('title_en', 'description_en', 'how_to_get_document_en')
        }),
        ('Hindi Localization', {
            'fields': ('title_hi', 'description_hi', 'how_to_get_document_hi'),
            'classes': ('collapse',),
        }),
        ('Marathi Localization', {
            'fields': ('title_mr', 'description_mr', 'how_to_get_document_mr'),
            'classes': ('collapse',),
        }),
        ('Filters & Eligibility', {
            'fields': ('category', 'state', 'caste', 'min_age', 'max_age', 'preferred_age', 'profession')
        }),
        ('Additional Fields', {
            'fields': ('image', 'required_for_application', 'issuing_authority')
        }),
    )

@admin.register(ServiceCenter)
class ServiceCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'center_type', 'city', 'state', 'pin_code', 'contact_number', 'timings')
    list_filter = ('center_type', 'state', 'city')
    search_fields = ('name', 'address', 'city', 'state', 'pin_code', 'services_offered')
    ordering = ('name',)
