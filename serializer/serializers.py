from rest_framework import serializers

from students.models import Student


def check_age(data):
    """
    自定义校验字段，这里的名字是可以随意的。
    :param data:
    :return:
    """
    if data > 100:
        raise serializers.ValidationError(detail="age cannot greater than 100")

    return data


class StudentSerializer(serializers.Serializer):
    SEX_OPTION = (
        (0, "unknown"),
        (1, "male"),
        (2, "female"),
    )
    #  用于生成Label标签或显示内容, help_text 提示信息
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20, label="name")
    age = serializers.IntegerField(label="age", validators=[check_age])
    sex = serializers.ChoiceField(choices=SEX_OPTION, label="sex") # choice字段
    classmate = serializers.CharField(max_length=15, label="class")
    description = serializers.CharField(allow_null=True, label="bio", allow_blank=True)

    def validate_name(self, data):
        """
        校验名字必须不能包含python， 注意这里的名字命名格式必须是validate_数据项的名字
        :param data: 传入的name字段
        :return: 必须将校验后的数据返回，否则就不能这个数据就成None了
        """
        if str(data).find("python") != -1:
            raise serializers.ValidationError(code="name", detail="python is a illegal word")
        return data

    def validate(self, attrs):
        """
        校验所有字段
        :param attrs: 这是所有的数据项，传入的是一个字典
        :return: 必须将校验后的数据返回，否则就不能这个数据就成None了
        """
        if attrs['sex'] != 1 and attrs["name"].find("Andy") == 2:
            raise serializers.ValidationError(code="sex_name", detail="Andy is not a  female")
        return attrs

    def create(self, validated_data):
        """
         重新写create方法，drf的Serializer只是写了接口，并没有实现，我们必须重新写
         :param validated_data:
         :return:
        """
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
         重新写update方法，drf的Serializer只是写了接口，并没有实现，我们必须重新写
         :param validated_data:
         :return:
        """
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


