from django.urls import path

from . import views

urlpatterns = [
    path("copies/", views.CopyView.as_view()),
    path("copies/<int:copy_id>/", views.CopyDetailView.as_view()),
]
