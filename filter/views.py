from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .authentication import CustomAuthentication
from students.models import Student
from students.serializers import StudentModelSerializer
from .permissions import IsAdminOrReadOnly

# class Students(APIView):
#     # authentication_classes = [CustomAuthentication, ]
#
#     def get(self, request):
#         if request.user.id is None:
#             return Response("未认证", status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response(f"the user: {request.user}")


class StudentView(ModelViewSet):
    # http://127.0.0.1:8000/filter/students/?ordering=-sex,age&sex=1
    # 过滤和排序应该要不一起全局，要不一起局部
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    filter_fields = ["sex"]
    ordering_fields = ["age", "sex"]
    # 自定义filter
    filter_backends = [DjangoFilterBackend, OrderingFilter]

