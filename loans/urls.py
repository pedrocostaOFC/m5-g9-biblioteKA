from django.urls import path
from django import views
from . import views

urlpatterns = [
    path('loan/', views.ListCreateLoanView.as_view()),
    path('loan/<int:pk>/', views.LoanDetailView.as_view()),
]