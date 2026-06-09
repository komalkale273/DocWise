from django.db import models
from django.contrib.auth.models import User

class userProfile(models.Model):
    EDUCATION_CHOICES = [
        ('primary', 'Primary School'),
        ('secondary', 'Secondary School'),
        ('higher_secondary', 'Higher Secondary (12th)'),
        ('undergraduate', 'Undergraduate (Bachelor Degree)'),
        ('postgraduate', 'Postgraduate (Master/PhD)'),
        ('none', 'None'),
    ]

    LIFE_STAGE_CHOICES = [
        ('newborn_parent', 'Parent of Newborn'),
        ('student', 'Student'),
        ('young_adult', 'Young Adult'),
        ('mid_age', 'Mid-Age Citizen'),
        ('senior_citizen', 'Senior Citizen'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    income = models.IntegerField(null=True)
    cast = models.CharField(null=False, max_length=100)
    state = models.CharField(null=False, max_length=100)
    profession = models.CharField(null=False, max_length=100)
    
    education_level = models.CharField(
        max_length=50,
        choices=EDUCATION_CHOICES,
        default='none',
        null=True,
        blank=True
    )
    
    life_stage = models.CharField(
        max_length=50,
        choices=LIFE_STAGE_CHOICES,
        default='young_adult',
        null=True,
        blank=True
    )

    preferred_language = models.CharField(
        max_length=10,
        choices=[
            ('en', 'English'),
            ('hi', 'Hindi'),
            ('mr', 'Marathi'),
            ('gu', 'Gujarati'),
            ('ta', 'Tamil'),
            ('te', 'Telugu'),
            ('bn', 'Bengali'),
            ('kn', 'Kannada'),
        ],
        default='en',
        null=True
    )

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username
