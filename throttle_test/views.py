from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from students.models import Student
from students.serializers import StudentModelSerializer


class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    throttle_scope = "student"
    throttle_classes = [AnonRateThrottle, UserRateThrottle, ScopedRateThrottle]
