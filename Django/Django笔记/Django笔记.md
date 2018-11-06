# Django笔记

- Django中内嵌了ORM框架，可以将类和数据表进行对应起来，只需要通过类和对象就可以对数据表进行操作。而不用写SQL语句。
- 生成迁移文件的作用：是把是把数据模型中的类的属性以及他的类型都把他拿过来，放到另一个文件，这个文件叫迁移文件。



管理员设置：

- 设置时区

```
# 在settings.py 中进行设置
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
```



**视图：**

例如，输入一个地址：localhost:8000/index发送请求之后--->经过Django框架处理后得到的只有‘/index’部分--> 把 ‘index’ 与项目的urls.py 中的文件进行匹配，比如以下代码：

```
from django.conf.urls import include, url
from django.contrib import admin

# 得到的'index'与URL中的正则表达式进行匹配，如果匹配成功，url中的第二个参数中的内容，哪个匹配成功就执行哪个
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('booktest.urls')),
]
```

```
# r'^$' 正则化表达式，如果符合第一个参数的正则表达式，那么久执行url中第二个参数的内容。
url(r'^$', views.index),
```


Django MySQL数据库配置：

在settings.py中的DATABASES进行配置：





![1539760010141](image\url_create.png)



