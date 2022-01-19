from rest_framework.serializers import ModelSerializer as Serializer

from students.models import Student


class StudentSerializer(Serializer):
    class Meta:
        model = Student
        fields = "__all__"
        ref_name = "mixin_generic_viewset_router"
