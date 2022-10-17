from django.urls import path

from apps import views

urlpatterns = [
    path('add/', views.add_index),
]
