from django.urls import path

from .views import TeachersListView, TeachersDetailView, CoursesDetailView, CoursesListView, StudentsListView,\
    StudentsDetailView

urlpatterns = [
    path("teachers/", TeachersListView.as_view()),
    path("teachers/<int:pk>/", TeachersDetailView.as_view()),

    path("courses/", CoursesListView.as_view()),
    path("courses/<int:pk>/", CoursesDetailView.as_view()),
    
    path("students/", StudentsListView.as_view()),
    path("students/<int:pk>/", StudentsDetailView.as_view())
]
