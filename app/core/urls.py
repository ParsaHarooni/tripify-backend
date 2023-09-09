from django.urls import path
from core import views

urlpatterns = [
    path('ping/', views.PingView.as_view(), name='ping'),
    path('trip/', view=views.TripView.as_view(), name='trip'),
    path('expense/', view=views.ExpenseView.as_view(), name='expense'),
    path('predict/', view=views.PredictPrice.as_view(), name='predict')
]
