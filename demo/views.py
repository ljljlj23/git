from django.http import HttpResponse
from django.template import Template, Context


def index(request):
    '''
    视图 函数视图
    :param request: 请求对象，包含了请求信息的一个请求对象
    :return: response:响应对象
    '''
    return HttpResponse('hello world')

def about(request):
    return HttpResponse('<h1>这是一个about页面</h1>')

def urltest(request,num):
    return HttpResponse('这是一个url测试%s'%num)

# def urltestnew(request,year,city):
#     return HttpResponse('%s年在%s'%(year,city))
def urltestnew(request,year,city):
    return HttpResponse('%s年在%s'%(year,city))

def gethtml(request):
    html='''
    <html>
    <head>
    </head>
    <body>
    <h1>一级标签</h1>
    <h2>{{ name }}</h2>
    <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1568004065249&di=ac15fb01c9ff9cf418dfe4736e807d3d&imgtype=0&src=http%3A%2F%2Fi-1.chuzhaobiao.com%2F2018%2F6%2F30%2FKDYwMHgp%2F029e8607-1c43-460e-bb42-4c367e4ac27e.jpg" alt='404'>
    <p style="font-size:28px;">{{ content }}</p>
    <a href="#">超链接</a>
    </body>
    </html>
    '''

    '''
    渲染数据步骤：
    '''
    # 1.构建模板结构
    template_obj=Template(html)
    # 2.创建渲染模板
    params=dict(name='表情包',content='段落')
    content_obj=Context(params)
    # 3.进行数据渲染
    result=template_obj.render(content_obj)
    # 4.返回结果
    return HttpResponse(result)

    # return HttpResponse(html)
'''
调用模板的方式
'''
# 1
from django.shortcuts import render

def indextmp(request):
    # return render(request,'index.html')

    name = '哈士奇'
    return render(request,'index.html',{'name':name})

# 2
from django.shortcuts import render_to_response

def abc(request):
    name = 'abcabcabc'
    return render_to_response('abc.html', {'name': name})

# 3
from django.template.loader import get_template

def hello(request):
    template=get_template('hello.html')
    name = 'hello html'
    return render_to_response('hello.html', {'name': name})

def tpltest(request,age):
    class Say(object):
        def say(self):
            return 'hello'

    name = 'zs'
    hobby = ['eat','sing','pingpang']
    score = {'math':100,'English':60}
    say=Say()
    myjs='''
    <script>
    alert('hello')
    </script>
    '''
    # return render(request,'tpltest.html',{'name':name,'age':age,'hobby':hobby,'score':score})
    # locals()函数，将所有局部变量返回
    return render(request,'tpltest.html',locals())

def statictest(request):
    return render(request,'statictest.html')

def staticdemo(request):
    # 球星排行榜
    params = [
        {"name": "麦迪", "img": "maidi.jpg",
         "url": "https://baike.baidu.com/item/%E7%89%B9%E9%9B%B7%E8%A5%BF%C2%B7%E9%BA%A6%E6%A0%BC%E9%9B%B7%E8%BF%AA/6118977?fromtitle=%E9%BA%A6%E8%BF%AA&fromid=136057&fr=aladdin"},
        {"name": "科比", "img": "kb.jpg", "url": "https://baike.sogou.com/v226587.htm?fromTitle=%E7%A7%91%E6%AF%94"},
        {"name": "姚明", "img": "ym.jpg", "url": "https://baike.sogou.com/v4957112.htm?fromTitle=%E5%A7%9A%E6%98%8E"},
        {"name": "易建联", "img": "yjl.jpg", "url": "https://baike.sogou.com/v17764.htm?fromTitle=%E6%98%93%E5%BB%BA%E8%81%94"},
    ]
    return render(request,'staticdemo.html',locals())