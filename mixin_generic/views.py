# from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# class StudentListView(ListAPIView, CreateAPIView):
class StudentListView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# class StudentDetailView(UpdateAPIView, RetrieveAPIView, DestroyAPIView):
class StudentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
