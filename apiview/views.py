from rest_framework.views import APIView as View
from rest_framework.response import Response
from rest_framework import status

from .serializers import StudentSerializer
from students.models import Student

# 使用APIView和view的两个区别就在于
# 1. 需要导入from rest_framework.views import APIView
# 2. request这个参数 将不再是之前的request，而是被drf处理的request
# 3. 可以直接使用Response返回数据， 不在需要JsonResponse了

class StudentListView(View):
    def get(self, request):
        """
        得到所有的学生信息
        :param request: request扩展了DJango中的request。
            request.data 返回的是前段传入的body。就像Django中的request.POST, request.FILES
                        他可以返回所有body数据，包括文件和非文件
            .query_params: request.GET。 因为并不是只有get方法可以通过地址栏传参，所以drf中重新写了这个函数
            .user: 用户
            如果想使用原生的request，这样调用： request._request.
        :return:
        """
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

