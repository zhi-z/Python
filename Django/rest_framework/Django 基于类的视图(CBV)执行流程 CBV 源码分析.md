# Django 基于类的视图(CBV)执行流程 CBV 源码分析



## 1 CBV(基于类的视图)

视图是可以调用的，它接受请求并返回响应，这不仅仅是一个函数，Django提供了一些可以用作视图的类的例子，这些允许您通过继承或mixin来构建视图并重用代码。

### 基本示例

Django提供了基本的视图类，它将适用于广泛的应用程序。所有的视图类都继承自View该类，它处理将视图链接到URL，HTTP方法调用和其他简单的功能。

在URLconf中简单使用

BookView是一个视图类，而不是一个函数，所以我们将URL指向as_view()类方法，它为基于类的视图提供了类似于函数的条目：

```
from django.conf.urls import url
from django.contrib import admin
from bookmanage import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'books/',views.BookView.as_view()),
]
```

BookView类

继承现有的View并覆盖父类中的方法。

```
from django.shortcuts import render,HttpResponse
from django.views import View


class BookView(View):

    def get(self,request):
        return HttpResponse('get....')

    def post(self,request):
        return HttpResponse('post....')
```

## 2 View

主要的基于类的基本视图，所有其他基于类的视图都是继承自这个View类，导入方式

```
from django.views import View
```

浏览器向服务器发送一个get请求，基于类的视图执行流程

首先，django启动，会执行视图类下的as_view()：

```
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # as_view()  执行类的as_view()   
    url(r'books/',views.BookView.as_view()),
]
```

as_view():由于BookView没有实现as_view()方法，会调用父类(View)中的as_view()方法：

self.dispatch():由于BookView没有实现dispatch()，所以会调用View类的dispatch()

主要作用：`view`视图的一部分 - 接受`request` 参数和参数的方法，并返回HTTP响应。

检测HTTP请求方法，并尝试委托给匹配HTTP方法的方法，一个`GET`将被委托给`get()`，一`POST`来`post()`，等等。

```
def dispatch(self, request, *args, **kwargs):
    # 尝试把用户请求分发到正确的方法，如果方法不存在，遵从错误的处理程序
    # 如果请求方法不在已批准的列表中，也会遵从错误的处理程序
    if request.method.lower() in self.http_method_names:
        #使用反射，例如用户访问是get请求
        # handler = getattr(BookView,"get",错误处理程序)
        handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
    else:
        handler = self.http_method_not_allowed
        
    # return get(request,*args, **kwargs)
    return handler(request, *args, **kwargs)
```

URLconf中的变化

```
此时URLconf的配置
 url(r'books/',views.BookView.as_view()),
 等价于
 url(r'books/',view) # 由于view return self.dispatch()
 等价于
 url(r'books/',self.dispatch())
 等价于
 url(r'books/',handler(request,*args,**kwargs)
 --> url(r'books/',get(request,*args,**kwargs)
 --> url(r'books/',post(request,*args,**kwargs)
 等等
```