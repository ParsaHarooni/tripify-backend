from django.urls import path
from core import views

urlpatterns = [
    path('ping/', views.PingView.as_view(), name='ping'),
    path('expense/', view=views.TripView.as_view(), name='expense'),
]
