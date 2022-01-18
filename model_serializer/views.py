from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView as View

from students.models import Student
from .serializers import StudentSerializer


@method_decorator(csrf_exempt, name='dispatch')
class StudentListView(View):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(instance=students, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        is_valid = serializer.is_valid()
        if is_valid is False:
            # print(serializer.error_messages)
            print(serializer.errors)
            # for key in serializer.errors:
            #     print(key)
            #     print(serializer.errors[key][0])
            return JsonResponse({"err": 1})
        else:
            print()
            student = serializer.save()
            return JsonResponse(StudentSerializer(instance=student).data)


class StudentDetailView(View):
    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        return JsonResponse(StudentSerializer(student).data)

    def put(self, request, pk):
        instance = Student.objects.get(pk=pk)
        serializer = StudentSerializer(data=request.data, instance=instance)
        serializer.is_valid(True)
        student = serializer.save()
        return JsonResponse(StudentSerializer(instance=student).data)

    def patch(self, request, pk):
        instance = Student.objects.get(pk=pk)
        serializer = StudentSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(True)
        student = serializer.save()
        return JsonResponse(StudentSerializer(instance=student).data)
