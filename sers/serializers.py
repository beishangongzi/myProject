from rest_framework import serializers

from students.models import Student


def check_age(data):
    if data > 100:
        raise serializers.ValidationError(detail="age cannot greater than 100")

    return data


class StudentSerializer(serializers.Serializer):
    SEX_OPTION = (
        (0, "unknown"),
        (1, "male"),
        (2, "female"),
    )
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20, label="name")
    age = serializers.IntegerField(label="age", validators=[check_age])
    sex = serializers.ChoiceField(choices=SEX_OPTION, label="sex")
    classmate = serializers.CharField(max_length=15, label="class")
    description = serializers.CharField(allow_null=True, label="bio", allow_blank=True)

    def validate_name(self, data):
        if str(data).find("python") != -1:
            raise serializers.ValidationError(code="name", detail="python is a illegal word")
        return data

    def validate(self, attrs):
        if attrs['sex'] != 1 and attrs["name"].find("Andy") == 2:
            raise serializers.ValidationError(code="sex_name", detail="Andy is not a  female")
        return attrs

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        keys = validated_data.keys()
        if "name" in keys:
            instance.name = validated_data["name"]
        if "age" in keys:
            instance.age = validated_data["age"]
        if "sex" in keys:
            instance.sex = validated_data["sex"]
        if "description" in keys:
            instance.description = validated_data["description"]
        if "classmate" in keys:
            instance.classmate = validated_data["classmate"]
        instance.save()
        return instance


