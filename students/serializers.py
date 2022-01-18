from rest_framework import serializers

# serializers.Serializers
# serializers.ModelSerializer

from .models import Student


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        # fields = ["id", "name"]
