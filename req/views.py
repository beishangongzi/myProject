from rest_framework.views import APIView as View
from rest_framework.response import Response
from rest_framework.status import *

from school.models import Student
from .serializers import StudentSerializer


class StudentView(View):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        print(request.user)
        print(request.user.is_staff)
        print(request.query_params)
        print(request.data)
        print(request.FILES)
        print(request.META)
        # return Response(serializer.data, status=HTTP_200_OK, content_type="application/json")
        return Response(serializer.data, status=HTTP_200_OK, content_type="text/html", headers={"name": "andy"})
