from django.db import models
from teachers.models import Teacher
# Create your models here.
class Course(models.Model):

    name=models.CharField(max_length=50) #课程名
    teacher=models.ForeignKey(Teacher, on_delete=models.DO_NOTHING) #教师
    coursetime=models.TextField(blank=True) #时间
    courseacademy=models.CharField(max_length=30) #开课单位
    credits=models.FloatField()#学分
    compulsory=models.BooleanField(default=False) #是否必修
    typeofcourse=models.CharField(max_length=20) #课程类别
    description=models.TextField(blank=True) #描述
    campus=models.CharField(max_length=20) #校区
    show=models.BooleanField(default=True) #是否展示
    
    def __str__(self):
        return self.name
