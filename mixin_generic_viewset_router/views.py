from rest_framework import status
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,\
    DestroyModelMixin
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import StudentSerializer
from students.models import Student


# class StudentListView(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
class StudentListView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(methods=["get"],  detail=False) #detail 是否自动生成pk
    def login(self, request):
        return Response("welcome you")
