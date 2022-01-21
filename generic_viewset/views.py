from rest_framework import status
from rest_framework.viewsets import GenericViewSet as View
from rest_framework.response import Response

from .serializers import StudentSerializer
from students.models import Student


class StudentListView(View):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request):
        """
        获取所有实体
        :param request:
        :return:
        """
        serializers = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializers.data)

    def create(self, request):
        """
        创建一个实体
        :param request:
        :return:
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(True)
        instance = serializer.save()
        return Response(self.serializer_class(instance).data)


    def retrieve(self, request, pk):
        """
        获取id是pk的实体
        :param request:
        :param pk:
        :return:
        """
        instance = self.get_object()
        return Response(self.get_serializer(instance).data)

    def update(self, request, pk):
        """
        更新
        :param request:
        :param pk:
        :return:
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, request.data)
        serializer.is_valid(True)
        return Response(self.get_serializer(serializer.save()).data)

    def partial_update(self, request, pk):
        """
        部分更新
        :param request:
        :param pk:
        :return:
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, request.data, partial=True)
        serializer.is_valid(True)
        return Response(self.get_serializer(serializer.save()).data)

    def destroy(self, request, pk):
        """
        删除某个实体
        :param request:
        :param pk:
        :return:
        """
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    