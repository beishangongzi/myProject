from rest_framework import serializers

from .models import Teacher, Student, Achievement, Course


class _TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ["name", "sex", "course"]


class CourseSerializer(serializers.ModelSerializer):
    # teacher = _TeacherSerializer()
    # 多对一或者一对一的数据表。
    #teacher = serializers.CharField(source="teacher.name")
    class Meta:
        model = Course
        fields = ["name", "teacher"]
        # 第三种
        depth = 1

class TeacherSerializer(serializers.ModelSerializer):
    class _CourseSerializer(serializers.ModelSerializer):
        class Meta:
            model = Course
            fields = ["name"]
    course = _CourseSerializer(many=True)

    class Meta:
        model = Teacher
        fields = ["name", "sex", "course"]
        # depth = 3




class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ["name", "s_achievement"]
        # depth = 1

        fields = ["name", "achievement"]

