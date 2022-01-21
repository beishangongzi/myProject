from rest_framework import serializers

from students.models import Student

# ModelSerializer继承自Serializer，这个类是和我们定义的模型紧密相关的，如果我们想操作数据库中数据，建议使用
# ModelSerializer，如果前段传入的数据不需要涉及数据库中增删改查，那么建议使用Serializer。
# ModelSerializer与Serializer相比，特别的地方在这三点
# 1. 它根据定义的模型，自动生成序列化器的字段
# 2. 会生成其它的验证算子，比如 unique_together. 这个是说多个数据项在一块应该是唯一的
# 3. 它重新了create和update方法。

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=10,
                                 write_only=True)  # 这个users是新加的，也就是说我们的model里面是没有的，但是可能我们需要用user做一些其他的事情，比如说验证
    classmate = serializers.RegexField("^\d{3}$")

    class Meta:
        model = Student  # 这里需要指定我们需要的模型
        fields = ["id", "name", "classmate", "sex", "description", "age", "user"]  # 这里是我们需要的字段，这里我加了我们需要的user
        # fields = "__all__" # 这里是包含我们需要的全部字段，但是不包括我们自己加的user
        # exclude = ["sex"] # 这是说sex其它字段都需要
        read_only_fields = [
            "id"]  # 这里是说 id只有反序列化的时候才会用到，如果是序列化，那么不需要检查这个字段，就算前段提交了也是没有用的，但是id在ModelSerializer中默认是只读的本就就
        ref_name = "model_serializer"  # 这个字段用来生成api的时候，需要给序列化器模型起一个别名，这个就是别名，现在可以不加。

        # 这是一些其它的参数，将错误信息换成我们自定义的信息。大家可以故意传错一个数据，比如名称传20个字符，那么就会报错，提示是我们自定义的信息
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

    # 这个是自定义验证
    def validate_user(self, data):
        if data != "root":
            raise serializers.ValidationError(code="user", detail="user must be root")

    # 因为我们传入了user，这个在模型中是没有的，所以应该重写create函数，将user删除
    def create(self, validated_data):
        validated_data.pop("user")
        return super(StudentSerializer, self).create(validated_data)
