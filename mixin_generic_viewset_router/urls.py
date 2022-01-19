from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import StudentListView

urlpatterns = [
]

router = DefaultRouter()
router.register("students", viewset=StudentListView, basename="stu")
urlpatterns += router.urls


