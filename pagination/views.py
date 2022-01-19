from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

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

class MyPagination(PageNumberPagination):
    page_size = 1
    page_query_param = "pg"  # default page
    page_size_query_param = 'size'  # default page_size
    max_page_size = 20  # 允许客户端自定义最大的值

class StudentView(ModelViewSet):
    # http://127.0.0.1:8000/filter/students/?ordering=-sex,age&sex=1
    # 过滤和排序应该要不一起全局，要不一起局部
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    filter_fields = ["sex"]
    ordering_fields = ["age", "sex"]
    # 自定义filter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    pagination_class = MyPagination
    # pagination_class = None # 禁止分页


    # 读取配置信息的方法
    # from django.conf import settings
    # from rest_framework.settings import api_settings
    # print(api_settings.DEFAULT_PAGINATION_CLASS)

