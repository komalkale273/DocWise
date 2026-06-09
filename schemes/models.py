from django.db import models
from documents.models import Documents
from django.contrib.auth.models import User
import datetime

class Schemes(models.Model):
    SCHEME_TYPE_CHOICES = [
        ('government', 'Government'),
        ('private', 'Private'),
    ]

    title_en = models.CharField(max_length=100)
    title_hi = models.CharField(max_length=100, blank=True, null=True)
    title_mr = models.CharField(max_length=100, blank=True, null=True)

    description_en = models.TextField()
    description_hi = models.TextField(blank=True, null=True)
    description_mr = models.TextField(blank=True, null=True)

    scheme_application_start_date = models.DateField(null=True, blank=True)
    deadline_scheme_application = models.DateField(null=True, blank=True)

    age_limit = models.IntegerField()
    income_limit = models.IntegerField()
    caste = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    category = models.CharField(max_length=100, null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)  # <-- Add this
    date_created = models.DateTimeField(default=datetime.datetime.now)
    required_documents = models.ManyToManyField(Documents)

    scheme_type = models.CharField(max_length=20, choices=SCHEME_TYPE_CHOICES, default='government')

    # Methods for handling multilingual content
    def get_localized_title(self, lang):
        return getattr(self, f"title_{lang}", self.title_en)

    def get_localized_description(self, lang):
        return getattr(self, f"description_{lang}", self.description_en)

    class Meta:
        indexes = [
            models.Index(fields=['state', 'age_limit', 'income_limit', 'scheme_type']),
        ]

    def __str__(self):
        return f"{self.title_en} ({self.get_localized_title('en')}) - {dict(self.SCHEME_TYPE_CHOICES).get(self.scheme_type, 'Unknown')}"
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scheme = models.ForeignKey(Schemes, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50, choices=[('new', 'New Scheme'), ('deadline', 'Deadline')])
    
    def __str__(self):
        return f"{self.user.username} - {self.type} - {self.scheme.title_en}"