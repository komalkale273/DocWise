from django.db import models

class Documents(models.Model):
    # Filters
    state = models.CharField(max_length=100, null=True, blank=True)
    caste = models.CharField(max_length=100, null=True, blank=True)
    min_age = models.PositiveIntegerField(null=True, blank=True)
    max_age = models.PositiveIntegerField(null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)

    # Multilingual Title and Description
    title_en = models.CharField(max_length=200)
    title_hi = models.CharField(max_length=200, blank=True, null=True)
    title_mr = models.CharField(max_length=200, blank=True, null=True)

    description_en = models.TextField()
    description_hi = models.TextField(blank=True, null=True)
    description_mr = models.TextField(blank=True, null=True)

    category = models.CharField(max_length=150)
    preferred_age = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='documents/images/', null=True, blank=True)
    required_for_application = models.BooleanField(default=False)

    # Multilingual Instructions
    how_to_get_document_en = models.TextField(null=True, blank=True)
    how_to_get_document_hi = models.TextField(null=True, blank=True)
    how_to_get_document_mr = models.TextField(null=True, blank=True)

    issuing_authority = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def get_localized_title(self, lang):
        val = getattr(self, f"title_{lang}", self.title_en)
        return val if val else self.title_en

    def get_localized_description(self, lang):
        val = getattr(self, f"description_{lang}", self.description_en)
        return val if val else self.description_en

    def get_localized_how_to_get_document(self, lang):
        val = getattr(self, f"how_to_get_document_{lang}", self.how_to_get_document_en)
        return val if val else self.how_to_get_document_en

    def __str__(self):
        return self.title_en


class ServiceCenter(models.Model):
    CENTER_TYPES = [
        ('csc', 'Common Service Center (CSC)'),
        ('rto', 'RTO Office'),
        ('municipal', 'Municipal Corporation Office'),
        ('post_office', 'Post Office'),
        ('cyber_cafe', 'Cyber Café (Authorized)'),
        ('other', 'Other Government Office'),
    ]

    name = models.CharField(max_length=200)
    center_type = models.CharField(max_length=50, choices=CENTER_TYPES, default='csc')
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    timings = models.CharField(max_length=100, default='9:00 AM - 6:00 PM')
    services_offered = models.TextField(help_text='Comma separated list of services (e.g., Aadhaar Card, PAN Card)')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.city})"

