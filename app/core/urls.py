from django.urls import path
from core import views

urlpatterns = [
    path('ping/', views.PingView.as_view(), name='ping'),
]
