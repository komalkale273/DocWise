# schemes/management/commands/notify_deadlines.py
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from datetime import timedelta
from django.utils import timezone
from schemes.models import Schemes, Notification
from users.models import userProfile

class Command(BaseCommand):
    help = 'Notify users about schemes nearing deadline and send email notifications'

    def handle(self, *args, **kwargs):
        # Define the deadline notification threshold (e.g., 3 days before)
        deadline_date = timezone.now().date() + timedelta(days=3)

        # Get schemes with the deadline approaching
        schemes = Schemes.objects.filter(deadline=deadline_date)

        for scheme in schemes:
            # Get users that match the scheme's criteria
            matched_users = userProfile.objects.filter(
                age__lte=scheme.age_limit,
                income__lte=scheme.income_limit,
                cast=scheme.caste,
                state=scheme.state,
                profession=scheme.profession
            )

            for profile in matched_users:
                # Avoid sending duplicate notifications
                if not Notification.objects.filter(user=profile.user, scheme=scheme, type='deadline').exists():
                    # Create a notification in the database
                    Notification.objects.create(
                        user=profile.user,
                        scheme=scheme,
                        message=f"The deadline for scheme '{scheme.title_en}' is approaching!",
                        type='deadline'
                    )

                    # Send an email to the user
                    subject = f"Reminder: Scheme Deadline Approaching"
                    message = f"Dear {profile.user.username},\n\nThe deadline for the scheme '{scheme.title_en}' is approaching. Please apply soon!\n\nRegards,\nYour Scheme Platform"
                    recipient_list = [profile.user.email]

                    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

        self.stdout.write("Deadline notifications and emails sent.")
