from django.urls import path
from . import views

urlpatterns = [
   path('schemes/', views.scheme_list, name='scheme_list'), 
   path('recommended_schemes/', views.recommended_schemes, name='recommended_schemes'),
   path('schemes/<int:pk>/', views.scheme_detail, name='scheme_detail'),
   
]
