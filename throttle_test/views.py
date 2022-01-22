from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from students.models import Student
from students.serializers import StudentModelSerializer


class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    throttle_scope = "student"
    throttle_classes = [AnonRateThrottle, UserRateThrottle, ScopedRateThrottle] # 这是局部配置, 分别是匿名用户，登入的用户，以及使用scope定义的方法
