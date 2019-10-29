from django.db import models

# Create your models here.
#python manage.py makemigrations创建迁移文件
#python manage.py migrate创建mysql表
class User(models.Model):
    #创建内部类
    class Meta:
        db_table = 'user'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48,null=False)
    email = models.CharField(max_length=64,null=False,unique=True)
    password = models.CharField(max_length=128,null=False)
    def __rept__(self):
        return "".format(self.id,self.name)
    __str__=__rept__

class student(models.Model):
    class Meta:
        db_table = 'student'
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=50,null=False)
    cno = models.CharField(max_length=50,null=False)
    def __str__(self):
        return self.id
