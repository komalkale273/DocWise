from django.urls import path
from . import views
from users.views import user_login, user_logout, register

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', user_login, name='login'),
    path('change-language/', views.change_language, name='change_language'),
    path('notifications/', views.notifications_view, name='notifications'),
]