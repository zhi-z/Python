# Django视图与URL

在Django中，通过浏览器去请求一个页面时，使用视图函数来处理这个请求的，视图函数处理之后，要给浏览器返回页面内容。 "

## 1 视图函数的使用

### 1.1 定义视图函数

视图函数定义在views.py中。

> 例：
>
> ```
>    def index(request):
>        #进行处理。。。
>        return HttpResponse('hello python')
> ```

视图函数必须有一个参数request，进行处理之后，需要返回一个HttpResponse的类对象，hello python就是返回给浏览器显示的内容。

### 1.2 url配置

![url_config](E:\GitHub\Python\Django\5.视图与URL\image\url_config.png)

> 说明：
>
> url配置的目的是让建立url和视图函数的对应关系。url配置项定义在urlpatterns的列表中，每一个配置项都调用url函数。
>
> url函数有两个参数，第一个参数是一个正则表达式，第二个是对应的处理动作。
>
> - 配置url时，有两种语法格式：
>   - url(正则表达式，视图函数名)
>   - url(正则表达式，include(应用中的urls文件))

工作中在配置url时，首先在项目的urls.py文件中添加配置项时，并不写具体的url和视图函数之间的对应关系，而是包含具体应用的urls.py文件，在应用的urls.py文件中写url和视图函数的对应关系。



## 2 url匹配过程

在项目的urls.py文件中包含具体应用的urls.py文件，应用的urls.py文件中写url和视图函数的对应关系。 

