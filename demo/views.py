from django.http import HttpResponse
def index(request):
    '''
    视图 函数视图
    :param request: 请求对象，包含了请求信息的一个请求对象
    :return: response:响应对象
    '''
    return HttpResponse('hello world')

def about(request):
    return HttpResponse('这是一个about页面')

def urltest(request,num):
    return HttpResponse('这是一个url测试%s'%num)

# def urltestnew(request,year,city):
#     return HttpResponse('%s年在%s'%(year,city))
def urltestnew(request,year,city):
    return HttpResponse('%s年在%s'%(year,city))