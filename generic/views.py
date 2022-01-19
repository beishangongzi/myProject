from rest_framework import status
from rest_framework.generics import GenericAPIView as View
from rest_framework.response import Response

from .serializers import StudentSerializer
from students.models import Student


class StudentListView(View):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        serializers = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(True)
        instance = serializer.save()
        return Response(self.serializer_class(instance).data)


class StudentDetailView(View):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk):
        instance = self.get_object()
        return Response(self.get_serializer(instance).data)

    def put(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance, request.data)
        serializer.is_valid(True)
        return Response(self.get_serializer(serializer.save()).data)

    def patch(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance, request.data, partial=True)
        serializer.is_valid(True)
        return Response(self.get_serializer(serializer.save()).data)

    def delete(self, request, pk):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    