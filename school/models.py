from django.db import models
from django.utils import timezone as datetime


# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=15, verbose_name="name")
    age = models.SmallIntegerField(verbose_name="age")
    sex = models.BooleanField(default=False)

    class Meta:
        db_table = "sch_student"

    def achievement(self):
        qs = self.s_achievement.all()
        return [q.score for q in qs]

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    sex = models.BooleanField(default=False)

    class Meta:
        db_table = "sch_teacher"

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="course name")
    teacher = models.ForeignKey("Teacher", on_delete=models.DO_NOTHING,
                                related_name="course", db_constraint=False)

    class Meta:
        db_table = "sch_course"

    def __str__(self):
        return self.name


class Achievement(models.Model):
    score = models.DecimalField(default=0, max_digits=4, decimal_places=1, verbose_name="score")
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, related_name="s_achievement", db_constraint=False)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, related_name="s_achievement", db_constraint=False)

    class Meta:
        db_table = "sch_achievement"

    def __str__(self):
        return self.score
