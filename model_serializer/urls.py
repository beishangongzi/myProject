from django.urls import path, include

from . import views

urlpatterns = [
    path("students/", views.StudentListView.as_view()),
    path("students/<int:pk>", views.StudentDetailView.as_view())
]