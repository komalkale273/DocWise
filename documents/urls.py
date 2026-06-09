from django.urls import path
from . import views

urlpatterns = [
    path('documents/', views.document_list, name='documents'),
    path('documents/<int:pk>/', views.document_detail, name='document_detail'),
    path('centers/', views.center_list, name='center_list'),
]
