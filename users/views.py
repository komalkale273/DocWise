from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from users.forms import UserRegistrationForm, UserProfileFrom
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import userProfile

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileFrom(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            messages.success(request, "Registered and logged in successfully!")
            return redirect('home')
        else:
            print("User Form Errors:", user_form.errors)
            print("Profile Form Errors:", profile_form.errors)
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileFrom()

    return render(request, 'register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')


def change_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        if request.user.is_authenticated:
            profile, created = userProfile.objects.get_or_create(user=request.user)
            profile.preferred_language = language
            profile.save()
    return redirect(request.META.get('HTTP_REFERER', 'home'))


from schemes.models import Notification

def notifications_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    
    # Render notifications and then mark them as read
    unread_notifications = notifications.filter(is_read=False)
    unread_notifications.update(is_read=True)
    
    lang = 'en'
    if hasattr(request.user, 'userprofile') and request.user.userprofile.preferred_language:
        lang = request.user.userprofile.preferred_language
        
    return render(request, 'notifications.html', {
        'notifications': notifications,
        'selected_lang': lang,
    })