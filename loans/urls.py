from django.urls import path
from django import views
from . import views

urlpatterns = [
    path('loan/', views.ListCreateLoanView.as_view()),
    path('loan/return/<pk>/', views.UpdatedReturnView.as_view()),
    path('loan/user/<pk>/', views.RetrieveLoanView.as_view()),
    path('loan/all', views.ListCreateLoanView.as_view()),
    path('loan/<pk>/', views.DeletedLoanView.as_view())
]