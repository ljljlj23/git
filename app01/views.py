from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app01.models import Person, Publish, Book, Teacher


def index(request):
    return HttpResponse('hello world')

# 单表的增删改查
def addPerson(request):
    '''
    save方法
    '''
    # 第1种
    # person = Person(name='lisi',age=19,height=170,birthday='2019-08-01')
    # person.save()

    # 第2种
    # person = Person()
    # person.name = 'wangwu'
    # person.age = 23
    # person.height = 185
    # person.birthday = '1998-03-01'
    # person.save()
    '''
    create方法
    '''
    # 第1种
    # Person.objects.create(name='hhh', age=10, height=190)

    # 第2种
    # data = dict(name='xxx',age=21,height=187)
    # Person.objects.create(**data)

    return HttpResponse('添加数据')

def getPerson(request):
    '''
    all方法
    返回一个queryset，存放对象
    返回符合条件的所有数据
    '''
    # 若重写了模块类的__str__方法，可直接输出
    # data = Person.objects.all()
    # print(data)

    # 若没有需要使用这种方式
    # data = Person.objects.all()
    # for one in data:
    #     print(one.id)
    #     print(one.name)
    #     print(one.age)
    #     print(one.height)

    '''
    get方法
    返回的是一个对象
    有且只能有一条
    get常使用主键作为条件
    '''
    # data = Person.objects.get(id=1)
    # print(data.name)
    # print(data.age)
    # print(data.height)

    '''
    filter方法
    返回一个queryset，存放对象
    返回符合条件的所有数据
    '''
    # data = Person.objects.filter(name='wangwu')
    # for one in data:
    #     print(one.age)

    '''
    first方法
    返回一个对象
    返回符合条件的第一条数据
    '''
    # data = Person.objects.filter(name='wangwu').first()
    # print(data.id)
    # print(data.name)
    # print(data.age)
    # print(data.height)

    '''
    last方法
    返回一个对象
    返回符合条件的最后一条
    '''
    # data = Person.objects.filter(name='wangwu').last()
    # print(data.id)
    # print(data.name)
    # print(data.age)
    # print(data.height)

    '''
    order_by方法
    正--升序，负--降序
    '''
    # data = Person.objects.all().order_by('id')
    # for one in data:
    #     print(one.id)

    # data = Person.objects.all().order_by('-id')
    # for one in data:
    #     print(one.id)

    '''
    exclude方法
    返回一个queryset
    包含跟给定条件不符合的所有数据
    '''
    # data = Person.objects.exclude(name='zs')
    # for one in data:
    #     print(one.id)

    '''
    reverse方法
    对查询结果反向排序
    这个方法通常放在有排序的查询集后面使用
    排序：使用order_by或者模型类中的class Meta中使用odering = []
    '''
    # data = Person.objects.order_by('-id').reverse()
    # print(data)
    '''
    values方法
    返回的是一个queryset，内容不是对象，而是具体数据的字典
    '''
    # data = Person.objects.filter(name='wangwu').values()
    # print(data)
    '''
    count方法
    返回的是符合当前条件的数据的条数
    '''
    # data = Person.objects.filter(name='wangwu').count()
    # print(data)
    '''
    exists方法
    判断是否存在
    返回True或False
    '''
    # data = Person.objects.filter(name='zs').exists()
    # print(data)
    '''
    切片
    '''
    # data = Person.objects.all()[0:2]
    # print(data)
    '''
    判断
    '''
    # lt 小于
    # data = Person.objects.filter(id__lt=4)
    # print(data)
    # lte 小于等于
    # data = Person.objects.filter(id__lte=4)
    # print(data)
    # gt 大于
    # data = Person.objects.filter(id__gt=4)
    # print(data)
    # gte 大于等于
    # data = Person.objects.filter(id__gte=4)
    # print(data)
    # in 包含
    # data = Person.objects.filter(id__in = [1,2,3])
    # print(data)
    # range 范围
    # data = Person.objects.filter(id__range=[1, 5])
    # print(data)
    # startswitch   像like j%
    # data = Person.objects.filter(name__startswith='w')
    # print(data)
    # endswitch   像like %j
    # data = Person.objects.filter(name__endswith='u')
    # print(data)
    # __contain  包含  大小写敏感
    # data = Person.objects.filter(name__contains='w')
    # print(data)
    # __icontains  包含  大小写不敏感
    # data = Person.objects.filter(name__icontains='W')
    # print(data)

    return HttpResponse('查询数据')

def updatePerson(request):
    '''
    save方法
    先查询到数据，然后进行重新赋值，然后执行save进行保存
    '''
    # data = Person.objects.get(id=2)
    # data.name='dhdsd'
    # data.save()

    # data = Person.objects.filter(name='hhh')
    # for one in data:
    #     if one.id == 8:
    #         one.name='hjhs'
    #     one.save()

    '''
    update方法
    '''
    # Person.objects.filter(id=2).update(name='aaaa')

    return HttpResponse('更新数据')

def deletePerson(request):
    '''
    delete方法
    '''
    # Person.objects.filter(id=9).delete()

    return HttpResponse('删除数据')

# 一对多的增删改查
def addPB(request):
    # Publish.objects.create(name='清华出版社',address='北京')
    # Publish.objects.create(name='中国出版社',address='北京朝阳')
    # Publish.objects.create(name='河南出版社',address='洛阳')

    # Book.objects.create(name='python入门',publish_id = 1)
    # 第一种
    # publish = Publish.objects.get(name='中国出版社')
    # Book.objects.create(name='java',publish_id=publish.id)

    # 第二种
    # Book.objects.create(name='python核心编程',publish=Publish.objects.get(name='中国出版社'))

    # 第三种
    # 正向操作 从外键所在的表到关联表
    # book = Book()
    # book.name='笨办法学python'
    # book.publish = Publish.objects.get(name='河南出版社')
    # book.save()
    # 反向操作 从关联表到外键所在的表
    # publish_obj = Publish.objects.get(name='中国出版社')
    # publish_obj.book_set.create(name='pythonWeb开发')

    return HttpResponse('添加数据')

def getPB(request):
    # 第一种
    # publish = Publish.objects.get(name='中国出版社')
    # book = Book.objects.filter(publish_id=publish.id).all()
    # for x in book:
    #     print(x.name)
    # 第二种
    # 正向查询
    # book = Book.objects.filter(name='pythonWeb开发').first()
    # print(book.name)
    # print(book.publish)    # publish对象
    # print(book.publish.name)
    # 第三种
    # 反向查询
    # publish = Publish.objects.get(name='中国出版社')
    # book = publish.book_set.all()
    # for b in book:
    #     print(b.name)

    return HttpResponse('查询数据')

def updatePB(request):
    '''
    save
    '''
    book = Book.objects.get(id=1)
    book.publish = Publish.objects.get(name='中国出版社')
    book.save()

    '''
    update
    '''
    # Book.objects.filter(name='java').update(publish = Publish.objects.get(name='清华出版社'))

    # publish_obj = Publish.objects.get(name='清华出版社')
    # Book.objects.filter(name='python核心编程').update(publish=publish_obj)

    '''
    set
    反向
    '''
    # public = Publish.objects.get(name='河南出版社')
    # book = Book.objects.get(id=4)
    # book1 = Book.objects.get(id=3)
    # public.book_set.set([book,book1])

    return HttpResponse('更新数据')

def deletePB(request):

    # Book.objects.get(id=2).delete()
    # Publish.objects.get(name='清华出版社').delete()

    return HttpResponse('删除数据')

# 多对多的增删改查
def manytomanyadd(request):
    # Teacher.objects.create(name='laozhang',gender='女')
    # Teacher.objects.create(name='laobian',gender='男')
    # Teacher.objects.create(name='laoliu',gender='男')
    # Teacher.objects.create(name='laowang',gender='女')

    '''
    增加新数据 并创建关系
    '''
    # teacher_obj = Teacher.objects.filter(name='laozhang').first()
    # teacher_obj.person.create(name='秦秦',age=17,height=192)

    '''
    已存在的数据 创建关系
    '''
    # teacher_obj = Teacher.objects.filter(name='laowang').first()
    # person_obj = Person.objects.filter(name='aaaa').first()
    # teacher_obj.person.add(person_obj)

    # 反向
    # teacher_obj = Teacher.objects.filter(name='laoliu').first()
    # person_obj = Person.objects.filter(name='秦秦').first()
    # person_obj.teacher_set.add(teacher_obj)

    return HttpResponse('多对多增加')

def manytomanyget(request):
    # 正向
    # teacher_obj = Teacher.objects.filter(name='laoliu').first()
    # person = teacher_obj.person.all()
    # print(person)

    # 反向
    # person_obj = Person.objects.filter(name='秦秦').first()
    # teacher = person_obj.teacher_set.all().values()
    # print(teacher)

    return HttpResponse('多对多查询')

def manytomanyupdate(request):
    # 正向
    # 第一种 根据id
    # teacher_obj = Teacher.objects.filter(name='laoliu').first()
    # teacher_obj.person.set([1,2,3,4,5])
    # 第二种 放对象
    # teacher_obj = Teacher.objects.filter(name='laoliu').first()
    # person1 = Person.objects.filter(name='wangwu').first()
    # person2 = Person.objects.filter(name='hjhs').first()
    # teacher_obj.person.set([person1,person2])
    # 反向
    # 第一种
    # person_obj = Person.objects.filter(name='lisi').first()
    # person_obj.teacher_set.set([2])
    # 第二种
    # person_obj = Person.objects.filter(name='wangwu').first()
    # teacher_obj = Teacher.objects.filter(name='laobian').first()
    # person_obj.teacher_set.set([teacher_obj])

    return HttpResponse('多对多更新')

def manytomanydelete(request):
    '''
    remove
    解除对象之间的关系
    '''
    # 正向操作
    # person_obj = Person.objects.filter(name='秦秦').first()
    # teacher_obj = Teacher.objects.filter(name='laozhang').first()
    # teacher_obj.person.remove(person_obj)
    #反向操作
    # person_obj = Person.objects.filter(name='zs').first()
    # teacher_obj = Teacher.objects.filter(name='laoliu').first()
    # person_obj.teacher_set.remove(teacher_obj)
    '''
    delete
    删除对象数据，以及对象之间的关系
    '''
    # 正向操作
    # Teacher.objects.filter(name='laoliu').first().delete()
    # 反向操作
    # Person.objects.filter(name='wangwu').first().delete()

    return HttpResponse('多对多删除')

# 聚合函数
from django.db.models import Avg,Max,Min,Count,Sum,F,Q
def polymerization(request):
    # data = Person.objects.all().aggregate(Avg('age'))
    # print(data)
    # 可设置键名，还可连用
    # data = Person.objects.all().aggregate(avg=Avg('age'),sum=Sum('age'))
    # print(data)

    return HttpResponse('聚合函数')

# F对象
def Ftest(request):

    data = Book.objects.filter(num__gt = F('salled')).all()
    print(data)

    return HttpResponse('F object test')

# Q对象
def Qtest(request):
    # and
    # data = Book.objects.filter(num=90,salled=100).all()
    # print(data)
    # or
    # data = Book.objects.filter(Q(num=10)|Q(salled=100)).all()
    # print(data)
    # not
    data = Book.objects.filter(~Q(num=10)|~Q(salled=20)).all()
    print(data)

    return HttpResponse('Q object test')