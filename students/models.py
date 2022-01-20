from django.db import models


# Create your models here.
# 注意写模型的时候，每个数据项后面前外不要加comma，否则django不报错，但是不会生成这个数据项
class Student(models.Model):
    SEX_OPTION = (
        (0, "unknown"),
        (1, "male"),
        (2, "female"),
    )
    # verbose_name 对象的可读名称，这是一个字符串，如果没有指认，比如 CamelCase 变成 camel case。
    # help_text 当用户输入这个表单的时候，收到的提示。
    name = models.CharField(max_length=20, verbose_name="name", help_text="Student's name")
    age = models.SmallIntegerField(verbose_name="age", help_text="student's age")
    sex = models.SmallIntegerField(choices=SEX_OPTION, verbose_name="sex", default=0, help_text="student's sex")
    classmate = models.CharField(db_column="class", max_length=15, verbose_name="class", default="cs", help_text="student's calss")
    description = models.TextField(null=True, blank=True, verbose_name="bio", help_text="student's description")

    class Meta:
        db_table = 'db_student' # 使用的数据表，如果这个表已经存在了，name就不要使用 `makemigration 和 migrate 迁移数据库了`
        verbose_name = "student information" # 可读的形式
        verbose_name_plural = "student information" # 可读的复数形式
