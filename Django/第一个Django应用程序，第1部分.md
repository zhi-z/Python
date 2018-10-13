# 第一个Django应用程序，第1部分[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial01/#writing-your-first-django-app-part-1)

让我们通过例子来学习。

在本教程中，我们将引导您完成基本轮询应用程序的创建。

它由两部分组成：

- 一个公共站点，允许人们查看民意调查并在其中投票。
- 一个管理站点，允许您添加，更改和删除民意调查。

我们假设你已经[安装](https://docs.djangoproject.com/en/2.1/intro/install/)了[Django](https://docs.djangoproject.com/en/2.1/intro/install/)。您可以通过在shell提示符中运行以下命令（由$前缀表示）来告知Django已安装以及哪个版本：

```
$ python -m django --version
```

如果安装了Django，您应该会看到安装的版本。如果不是，您将收到错误消息“没有名为django的模块”。

本教程是为Django 2.1编写的，它支持Python 3.5及更高版本。如果Django版本不匹配，您可以使用本页右下角的版本切换器参考您的Django版本的教程，或者将Django更新到最新版本。如果你使用的是旧版本的Python，请检查[我可以使用哪些Python版本的Django？](https://docs.djangoproject.com/en/2.1/faq/install/#faq-python-version-support)找到Django的兼容版本。

有关[如何](https://docs.djangoproject.com/en/2.1/topics/install/)删除旧版本Django并安装较新版本的建议，请参阅[如何安装Django](https://docs.djangoproject.com/en/2.1/topics/install/)。

- 哪里可以获得帮助：如果您在阅读本教程时遇到问题，请发送消息给[django-users](https://docs.djangoproject.com/en/2.1/internals/mailing-lists/#django-users-mailing-list)或者通过[irc.freenode.net](irc://irc.freenode.net/django)上的[#django](irc://irc.freenode.net/django)与其他可能提供帮助的Django用户聊天。

## 创建项目[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial01/#creating-a-project)

如果这是你第一次使用Django，你将不得不处理一些初始设置。也就是说，您需要自动生成一些建立Django [项目的](https://docs.djangoproject.com/en/2.1/glossary/#term-project)代码- Django实例的设置集合，包括数据库配置，Django特定选项和特定于应用程序的设置。

从命令行`cd`进入要存储代码的目录，然后运行以下命令：

```
$ django-admin startproject mysite
```

这将`mysite`在当前目录中创建一个目录。如果它不起作用，请参阅[运行django-admin的问题](https://docs.djangoproject.com/en/2.1/faq/troubleshooting/#troubleshooting-django-admin)。

- 注意：您需要避免在内置Python或Django组件之后命名项目。特别是，这意味着你应该避免使用像 `django`（这将与Django本身冲突）或`test`（与内置Python包冲突）这样的名称。

让我们来看看[`startproject`](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-startproject)创造了什么：

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

这些文件是：

- 外部`mysite/`根目录只是项目的容器。它的名字对Django来说无关紧要; 你可以将它重命名为你喜欢的任何东西。
- `manage.py`：一个命令行实用程序，允许您以各种方式与此Django项目进行交互。您可以`manage.py`在[django-admin和manage.py中](https://docs.djangoproject.com/en/2.1/ref/django-admin/)阅读有关的所有详细信息 。
- 内部`mysite/`目录是项目的实际Python包。它的名称是您需要用来导入其中任何内容的Python包名称（例如`mysite.urls`）。
- `mysite/__init__.py`：一个空文件，告诉Python该目录应该被视为Python包。如果您是Python初学者，请阅读官方Python文档中[有关包的更多信息](https://docs.python.org/3/tutorial/modules.html#tut-packages)。
- `mysite/settings.py`：此Django项目的设置/配置。 [Django设置](https://docs.djangoproject.com/en/2.1/topics/settings/)将告诉您有关设置如何工作的所有信息。
- `mysite/urls.py`：这个Django项目的URL声明; 您的Django支持的站点的“目录”。您可以在[URL调度](https://docs.djangoproject.com/en/2.1/topics/http/urls/)程序中阅读有关URL的更多信息。
- `mysite/wsgi.py`：与WSGI兼容的Web服务器的入口点，用于为您的项目提供服务。有关更多详细信息，请参阅[如何使用WSGI](https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/)进行[部署](https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/)。

## 开发服务器[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial01/#the-development-server)

让我们验证您的Django项目是否有效。`mysite`如果尚未更改到外部目录，请运行以下命令：

```
$ python manage.py runserver
```

您将在命令行中看到以下输出：

```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

October 10, 2018 - 15:50:53
Django version 2.1, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

- **注意**

暂时忽略有关未应用数据库迁移的警告; 我们很快就会处理数据库。

您已经启动了Django开发服务器，这是一个纯粹用Python编写的轻量级Web服务器。我们已经将它包含在Django中，因此您可以快速开发，而无需处理配置生产服务器（如Apache），直到您准备好进行生产。

现在是时候注意了：**不要**在类似生产环境的任何地方使用这个服务器。它仅用于开发时使用。（我们的业务是制作Web框架，而不是Web服务器。）

现在服务器正在运行，请使用Web浏览器访问<http://127.0.0.1:8000/>。你会看到一个“祝贺！”页面，火箭起飞。有效！

- **改变端口**

默认情况下，该[`runserver`](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-runserver)命令在端口8000的内部IP上启动开发服务器。

如果要更改服务器的端口，请将其作为命令行参数传递。例如，此命令在端口8080上启动服务器：

```
$ python manage.py runserver 8080
```

如果要更改服务器的IP，请将其与端口一起传递。例如，要监听所有可用的公共IP（如果您正在运行Vagrant或想要在网络上的其他计算机上展示您的工作，这很有用），请使用：

```
$ python manage.py runserver 0:8000
```

**0**是**0.0.0.0**的快捷方式。可以在[`runserver`](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-runserver)参考中找到开发服务器的完整文档。

自动重装 [`runserver`](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-runserver)

开发服务器根据需要自动为每个请求重新加载Python代码。您无需重新启动服务器即可使代码更改生效。但是，某些操作（如添加文件）不会触发重新启动，因此在这些情况下您必须重新启动服务器。

## 创建民意调查应用[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial01/#creating-the-polls-app)

既然你的环境 - 一个“项目” - 已经建立起来，你就可以开始工作了。

您在Django中编写的每个应用程序都包含一个遵循特定约定的Python包。Django附带了一个实用程序，可以自动生成应用程序的基本目录结构，因此您可以专注于编写代码而不是创建目录。

项目与应用

项目和应用程序之间有什么区别？应用程序是执行某些操作的Web应用程序 - 例如，Weblog系统，公共记录数据库或简单的轮询应用程序。项目是特定网站的配置和应用程序的集合。项目可以包含多个应用程序。一个应用程序可以在多个项目中。

您的应用程序可以存在于[Python路径的](https://docs.python.org/3/tutorial/modules.html#tut-searchpath)任何位置。在本教程中，我们将在您的`manage.py` 文件旁边创建我们的民意调查应用程序，以便可以将其导入为自己的顶级模块，而不是子模块`mysite`。

要创建应用程序，请确保您与该目录位于同一目录中`manage.py` 并键入以下命令：

```
$ python manage.py startapp polls
```

那将创建一个目录`polls`，其布局如下：

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

此目录结构将容纳轮询应用程序。

## 写下你的第一个视图[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial01/#write-your-first-view)

我们来写第一个视图。打开文件`polls/views.py` 并在其中放入以下Python代码：

民调/的views.py [¶](https://docs.djangoproject.com/en/2.1/intro/tutorial01/#id1)

```
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

这是Django中最简单的视图。要调用视图，我们需要将其映射到URL - 为此我们需要一个URLconf。

要在polls目录中创建URLconf，请创建一个名为的文件`urls.py`。您的app目录现在应该如下所示：

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

在该`polls/urls.py`文件中包含以下代码：

民调/的urls.py [¶](https://docs.djangoproject.com/en/2.1/intro/tutorial01/#id2)

```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

下一步是将根URLconf指向`polls.urls`模块。在 `mysite/urls.py`，添加导入`django.urls.include`并[`include()`](https://docs.djangoproject.com/en/2.1/ref/urls/#django.urls.include)在`urlpatterns`列表中插入 ，所以你有：

mysite的/的urls.py [¶](https://docs.djangoproject.com/en/2.1/intro/tutorial01/#id3)

```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

该[`include()`](https://docs.djangoproject.com/en/2.1/ref/urls/#django.urls.include)函数允许引用其他URLconf。每当Django遇到时[`include()`](https://docs.djangoproject.com/en/2.1/ref/urls/#django.urls.include)，它都会删除与该点匹配的URL的任何部分，并将剩余的字符串发送到包含的URLconf以进行进一步处理。

背后的想法[`include()`](https://docs.djangoproject.com/en/2.1/ref/urls/#django.urls.include)是使即插即用的URL变得容易。由于民意调查位于他们自己的URLconf（`polls/urls.py`）中，因此可以将它们放在“/ polls /”下，或“/ fun_polls /”下，或“/ content / polls /”下，或任何其他路径根目录下，并且应用仍会工作。

- 什么时候用 [`include()`](https://docs.djangoproject.com/en/2.1/ref/urls/#django.urls.include)

`include()`当您包含其他URL模式时，应始终使用。 `admin.site.urls`是唯一的例外。

您现在已将`index`视图连接到URLconf。让我们验证它是否正常工作，运行以下命令：

```
$ python manage.py runserver
```

在浏览器中转到[http：// localhost：8000 / polls /](http://localhost:8000/polls/)，您应该看到文本“ *Hello，world。你在民意调查指数。*“，您在`index`视图中定义的 。

找不到网页？

如果您在此处获得错误页面，请检查您是否要访问 [http：// localhost：8000 / polls /](http://localhost:8000/polls/)而不是[http：// localhost：8000 /](http://localhost:8000/)。

该[`path()`](https://docs.djangoproject.com/en/2.1/ref/urls/#django.urls.path)函数传递了四个参数，两个必需： `route`和`view`，以及两个可选：`kwargs`，和`name`。在这一点上，值得回顾一下这些论点的用途。

### [`path()`](https://docs.djangoproject.com/en/2.1/ref/urls/#django.urls.path)参数：`route`[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial01/#path-argument-route)

`route`是包含URL模式的字符串。处理请求时，Django从第一个模式开始`urlpatterns`并沿着列表向下移动，将请求的URL与每个模式进行比较，直到找到匹配的模式。

模式不搜索GET和POST参数或域名。例如，在请求中`https://www.example.com/myapp/`，URLconf将查找 `myapp/`。在请求中`https://www.example.com/myapp/?page=3`，URLconf也会查找`myapp/`。

### [`path()`](https://docs.djangoproject.com/en/2.1/ref/urls/#django.urls.path)参数：`view`[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial01/#path-argument-view)

当Django找到匹配的模式时，它调用指定的视图函数，其中一个[`HttpRequest`](https://docs.djangoproject.com/en/2.1/ref/request-response/#django.http.HttpRequest)对象作为第一个参数，并且路由中的任何“捕获”值作为关键字参数。我们稍后会给出一个例子。

### [`path()`](https://docs.djangoproject.com/en/2.1/ref/urls/#django.urls.path)参数：`kwargs`[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial01/#path-argument-kwargs)

任意关键字参数可以在字典中传递到目标视图。我们不打算在教程中使用Django的这个功能。

### [`path()`](https://docs.djangoproject.com/en/2.1/ref/urls/#django.urls.path)参数：`name`[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial01/#path-argument-name)

命名您的URL可让您从Django的其他地方明确地引用它，尤其是在模板中。此强大功能允许您在仅触摸单个文件的同时对项目的URL模式进行全局更改。