from django.db import models

# Create your models here.
class Person(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    height = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='身高')
    birthday = models.DateField(verbose_name='生日',null=True,auto_now=True)

    class Meta:
        db_table = 'person'
        verbose_name = '用户'
        # 去掉s
        verbose_name_plural = verbose_name
        # ordering=['-id','age']

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=8)
    person = models.ManyToManyField(to=Person)

    def __str__(self):
        return self.name

    class Meta:
        db_table='teacher'


class Publish(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=32)

    class Meta:
        db_table = 'publish'

class Book(models.Model):
    name = models.CharField(max_length=32)
    # to 设置关联表
    # to_feild 关联表要关联的键名，默认为关联表中的id，可以不写
# 级联等级
    # CASCADE 当关联表中数据删除的时候，外键所在表中的数据也会被删除
    # SET_NULL 当关联表中数据删除的时候，外键所在表中的外键设置为空
    # SET_DEFAULT 当关联表中数据删除的时候，为外键所在表中的外键设置一个默认值
    # PROTECT 关联保护，当关联表中数据被删除的时候，报异常
    # DO_NOTHING 当关联表中数据被删除的时候，外键所在的表不进行任何操作
    num = models.IntegerField(default=10)
    salled = models.IntegerField(default=10)
    publish = models.ForeignKey(to=Publish,to_field='id',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book'

