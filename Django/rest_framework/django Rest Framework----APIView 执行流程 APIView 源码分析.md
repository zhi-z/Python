# django Rest Framework----APIView 执行流程 APIView 源码分析

## 1 as_view()

我们还是先从URLconfig中入手，由于BookView是一个基于类的视图，所以我们将URL指向as_view()类方法

```
url(r'books/',views.BookView.as_view()),
```

此时，我们的BookView已经不是继承自django.views中View了，而是restframework.views中的APIView

安装Django RestFramework

```
pip install djangorestframework
```

BookView视图类：

```
from django.shortcuts import render,HttpResponse
#导入APIView
from rest_framework.views import APIView

#继承自APIView
class BookView(APIView):

    def get(self,request):
        return HttpResponse('get....')

    def post(self,request):
        return HttpResponse('post....')
```

as_view():由于BookView没有实现as_view()方法，django启动时，调用的as_view()是APIView中的as_view()

```
@classmethod
def as_view(cls, **initkwargs):
    """
    将原始类存储在视图函数上
    这允许我们在执行url反向查找时发现有关视图的信息。
    """
    ...
    #由于APIView是继承自django.views中的View(上篇博客接触过)
    #调用父类(View)中的as_view()
    view = super(APIView, cls).as_view(**initkwargs)
    view.cls = cls
    view.initkwargs = initkwargs

    # 提示: 基于会话的身份验证被明确地CSRF验证
    # 所有其他身份验证都免予使用CSRF。
    # 跳过CSRF验证
    return csrf_exempt(view)
```

在APIView中的as_view()方法什么都没做，只是调用了父类的as_view()方法

之前的博客介绍过，as_view()方法会返回self.dispatch() ，由于BookView没有实现这个方法，所以我们查看APIView中dispatch()都做了哪些工作

dispatch():和Djnago.views中View类的dispatch()派遣相同，额外添加了一些功能

```
# Note: 在“派遣”需要被改写的情况下，可以在"as_view"范围内对CSRF进行豁免，以防止意外移除这一豁免。
def dispatch(self, request, *args, **kwargs):
    """
    和django.views中View的dispatch()调度差不多,
    但是有额外的钩子用于启动、终结和异常处理。
    """
    self.args = args
    self.kwargs = kwargs
    request = self.initialize_request(request, *args, **kwargs)
    self.request = request
    self.headers = self.default_response_headers  # deprecate?
    try:
        self.initial(request, *args, **kwargs)

        # 获取适当的程序处理方法，这里的调度和django  View的调度一样
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(),
                              self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        
        # 调用HTTP请求处理方法，并返回
        response = handler(request, *args, **kwargs)

    except Exception as exc:
        response = self.handle_exception(exc)

    self.response = self.finalize_response(request, response, *args, **kwargs)
    return self.response
```

APIView中的dispatch()和Django中的dispatch()类似，不同之处，APIView对request请求对象进行了重新封装

request：APIView对request对象进行了重新封装

```
def dispatch(self, request, *args, **kwargs):
    """
    `.dispatch()` is pretty much the same as Django's regular dispatch,
    but with extra hooks for startup, finalize, and exception handling.
    """
    self.args = args
    self.kwargs = kwargs
    request = self.initialize_request(request, *args, **kwargs)
    self.request = request
    self.headers = self.default_response_headers  # deprecate?
    
    ....
```

默认的是django.core.handlers.wsgi.WSGIRequest对象，通过调用initialize_request()将其封装成rest_framework.request.Request。通过type(request)来查看

initialize_request():做了哪些工作

```
def initialize_request(self, request, *args, **kwargs):
    parser_context = self.get_parser_context(request)

    # 返回了一个reuqest请求对象
    return Request(
        request,
        parsers=self.get_parsers(),
        authenticators=self.get_authenticators(),
        negotiator=self.get_content_negotiator(),
        parser_context=parser_context
    )
```

Request类: 完善`request`请求的一些注意事项，例如用户登录、检测权限等等

```
class Request(object):

    def __init__(self, request, parsers=None, authenticators=None,
                 negotiator=None, parser_context=None):
        ...
        #将原始的WSGIReqeust对象复制给_request
        self._request = request

        ....

    #调用旧的request.GET
    @property
    def query_params(self):return self._request.GET
    
    #调用旧的request.POST
    @property
    def POST(self):return QueryDict('', encoding=self._request._encoding)    
```

之后使用的request，都是restfromwork封装的Reqeust对象。