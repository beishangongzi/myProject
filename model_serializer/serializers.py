from rest_framework import serializers

from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=10, write_only=True)
    classmate = serializers.RegexField("^\d{3}$")
    class Meta:
        model = Student
        fields = ["id", "name", "classmate", "sex", "description", "age", "user"]
        # fields = "__all__"
        # exclude = ["user"]
        read_only_fields = ["id"]

        extra_kwargs = {
            "name": {
                "error_messages": {
                    "max_length": "student's name can not more than 15 characters.",
                    "null": "student's name con not be null.",
                    "blank": "student's name can not be blank.",
                    "required": "student's name is required."
                }
            },
            "age": {
                "max_value": 50,
                "min_value": 18,
                "error_messages": {
                    "max_value": "Ensure age is less than or equal to 50",
                    "min_value": "Ensure age is great then or equal to 18"
                }
            },
            "classmate": {
                "error_messages": {
                    "invalid": "the value must be integer"
                }
            }
        }

    def validate_user(self, data):
        if data != "root":
            raise serializers.ValidationError(code="user", detail="user must be root")

    def create(self, validated_data):
        validated_data.pop("user")
        return super(StudentSerializer, self).create(validated_data)