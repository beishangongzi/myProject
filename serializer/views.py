from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView as View

from students.models import Student
from .serializers import StudentSerializer


@method_decorator(csrf_exempt, name='dispatch') # 前后端分离的时候解决跨域问题 如果不明白可以百度csrf
class StudentListView(View):
    def get(self, request):
        """
        查看所有学生的信息
        :param request:
        :return:
        """
        students = Student.objects.all()
        serializer = StudentSerializer(instance=students, many=True) # 是多个学生的信息，所以设置many=True
        return JsonResponse(serializer.data, safe=False)  # 因为返回的是多个学生的信息，也就是说返回的是一个列表，所以设置safe=False

    def post(self, request):
        """
        增加一个学生的信息
        :param request:
        :return:
        """
        serializer = StudentSerializer(data=request.data)
        is_valid = serializer.is_valid() # 在反序列化的时候，应该将数据验证一下，这里可以传入一个参数 raise_exception=True, 这样就会跑出异常如果数据是不合法的
        if is_valid is False:
            print(serializer.error_messages)
            print(serializer.errors)
            for key in serializer.errors:
                print(key)
                print(serializer.errors[key][0])
            return JsonResponse({"err": 1})
        else:
            print()
            student = serializer.save() # 存储学生的信息
            return JsonResponse(StudentSerializer(instance=student).data)  # 返回存储的学生信息


class StudentDetailView(View):
    def get(self, request, pk):
        """
        得到一个学生的信息
        :param request:
        :param pk: 学生的id
        :return:
        """
        student = Student.objects.get(pk=pk)
        return JsonResponse(StudentSerializer(student).data)

    def put(self, request, pk):
        """
        修改学生的信息，这里学生的所有信息必须全部提交
        :param request:
        :param pk:
        :return:
        """
        instance = Student.objects.get(pk=pk)
        serializer = StudentSerializer(data=request.data, instance=instance)
        serializer.is_valid(True)
        student = serializer.save()
        return JsonResponse(StudentSerializer(instance=student).data)

    def patch(self, request, pk):
        """
        修改部分数据
        :param request:
        :param pk:
        :return:
        """
        instance = Student.objects.get(pk=pk)
        serializer = StudentSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(True)
        student = serializer.save()
        return JsonResponse(StudentSerializer(instance=student).data)
