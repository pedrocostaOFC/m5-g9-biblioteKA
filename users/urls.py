from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path('users/follow-book/', views.UserBookViewDetail.as_view(), name='follow_book'),
    path('users/unfollow-book/<int:pk>/', views.UnfollowBookView.as_view(), name='unfollow-book'),
]