from rest_framework.views import APIView as View
from django.http.response import JsonResponse

from .models import Teacher, Course, Student
from .serializers import TeacherSerializer, CourseSerializer, StudentSerializer


class TeachersListView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(instance=teachers, many=Teacher)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        serializer.is_valid(True)
        teacher = serializer.save()
        return JsonResponse(TeacherSerializer(teacher).data)


class TeachersDetailView(View):
    def get(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherSerializer(instance=teacher)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherSerializer(instance=teacher, data=request.data)
        serializer.is_valid(True)
        teacher = serializer.save()
        return JsonResponse(TeacherSerializer(teacher).data)

    def patch(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherSerializer(instance=teacher, data=request.data, partial=True)
        serializer.is_valid(True)
        teacher = serializer.save()
        return JsonResponse(TeacherSerializer(teacher).data)


class CoursesListView(View):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(instance=courses, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(True)
        course = serializer.save()
        return JsonResponse(CourseSerializer(course).data)


class CoursesDetailView(View):
    def get(self, request, pk):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(instance=course)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(instance=course, data=request.data)
        serializer.is_valid(True)
        course = serializer.save()
        return JsonResponse(CourseSerializer(course).data)

    def patch(self, request, pk):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(instance=course, data=request.data, partial=True)
        serializer.is_valid(True)
        course = serializer.save()
        return JsonResponse(CourseSerializer(course).data)


class StudentsListView(View):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(instance=students, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(True)
        student = serializer.save()
        return JsonResponse(StudentSerializer(student).data)


class StudentsDetailView(View):
    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(instance=student)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        serializer.is_valid(True)
        student = serializer.save()
        return JsonResponse(StudentSerializer(student).data)

    def patch(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(instance=student, data=request.data, partial=True)
        serializer.is_valid(True)
        student = serializer.save()
        return JsonResponse(StudentSerializer(student).data)
