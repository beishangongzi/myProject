from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter

from . import views


urlpatterns = [
    path("students/", views.StudentListView.as_view()),
    path("students/<int:pk>", views.StudentDetailView.as_view())
]

# router = DefaultRouter()
# router.register("students", viewset=views.StudentModelViewSet, basename="stu")
# urlpatterns += router.urls
