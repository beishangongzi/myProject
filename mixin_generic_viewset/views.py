from rest_framework import status
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,\
    DestroyModelMixin
from rest_framework.response import Response

from .serializers import StudentSerializer
from students.models import Student


# class StudentListView(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
class StudentListView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
