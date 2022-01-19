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

    # 读取配置信息的方法
    # from django.conf import settings
    # from rest_framework.settings import api_settings
    # print(api_settings.DEFAULT_PAGINATION_CLASS)

    # Rest framework 本身在apiview中提供了异常处理，但是仅仅对drf内部现有的接口开发相关的异常进行格式处理，但是在开发中我们还会使用各种数据和进行何各种网络请求，浙西异常在django restframework中没有处理，多以抛给了django，django会组织错信息返回给客户端，我们应该写成json格式
    def list(self, request, *args, **kwargs):
        1/0
        return super(StudentView, self).list(request, *args, **kwargs)
    