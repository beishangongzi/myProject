from rest_framework.views import APIView as View
from rest_framework.response import Response
from rest_framework import status

from .serializers import StudentSerializer
from students.models import Student


class StudentListView(View):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(True)
        print(serializer.validated_data)
        student = serializer.save()
        return Response(StudentSerializer(student).data, status=status.HTTP_201_CREATED)


class StudentDetailView(View):
    def get(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            return Response(StudentSerializer(student).data)
        except Student.DoesNotExist:
            return Response({"msg": "the student is not in db"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student, data=request.data)
            serializer.is_valid(True)
            student = serializer.save()
            return Response(StudentSerializer(student).data)
        except Student.DoesNotExist:
            return Response({"msg": "the student is not in db"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student, data=request.data, partial=True)
            serializer.is_valid(True)
            student = serializer.save()
            return Response(StudentSerializer(student).data)

        except Student.DoesNotExist:
            return Response({"msg": "the student is not in db"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response({"msg": "the student is not in db"}, status=status.HTTP_404_NOT_FOUND)

