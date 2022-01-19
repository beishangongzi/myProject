from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import StudentView
urlpatterns = [

]

router = DefaultRouter()
router.register("students", viewset=StudentView, basename="stu")
urlpatterns += router.urls
