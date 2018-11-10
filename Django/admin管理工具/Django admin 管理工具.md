# Django admin 管理工具

## 1 admin组件的使用

Django 提供了基于 web 的管理工具。

Django 自动管理工具是 django.contrib 的一部分。你可以在项目的 settings.py 中的 INSTALLED_APPS 看到它：

```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "app01"
]
```

django.contrib是一套庞大的功能集，它是Django基本代码的组成部分。

**1. 激活管理工具**

通常我们在生成项目时会在 urls.py 中自动设置好，

```
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

]
```

当这一切都配置好后，Django 管理工具就可以运行了。

**2. 使用管理工具**

启动开发服务器，然后在浏览器中访问 http://127.0.0.1:8000/admin/，得到登陆界面，你可以通过命令 **python manage.py createsuperuser** 来创建超级用户。

为了让 admin 界面管理某个数据模型，我们需要先注册该数据模型到 admin

```
from django.db import models

# Create your models here.

class Author(models.Model):

    name=models.CharField( max_length=32)
    age=models.IntegerField()

    def __str__(self):
        return self.name

class Publish(models.Model):

    name=models.CharField( max_length=32)
    email=models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):

    title = models.CharField( max_length=32)
    publishDate=models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2)

    publisher=models.ForeignKey(to="Publish")
    authors=models.ManyToManyField(to='Author')

    def __str__(self):
        return self.title
```

**3. admin的定制**

在admin.py中只需要讲Mode中的某个类注册，即可在Admin中实现增删改查的功能，如：

```
admin.site.register(models.UserInfo)
```

但是，这种方式比较简单，如果想要进行更多的定制操作，需要利用ModelAdmin进行操作，如：

```
方式一：
    class UserAdmin(admin.ModelAdmin):
        list_display = ('user', 'pwd',)
 
    admin.site.register(models.UserInfo, UserAdmin) # 第一个参数可以是列表
     
 
方式二：
    @admin.register(models.UserInfo)                # 第一个参数可以是列表
    class UserAdmin(admin.ModelAdmin):
        list_display = ('user', 'pwd',)

列表的意思就是可以同时注册，以免代码重复
```

ModelAdmin中提供了大量的可定制功能，如

 1. list_display，列表时，定制显示的列。

```
@admin.register(models.UserInfo)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'pwd', 'xxxxx')
```

2. list_display_links，列表时，定制列可以点击跳转到当前对象编辑页面。

```
@admin.register(models.UserInfo)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'pwd', 'xxxxx')
    list_display_links = ('pwd',)   
```

3. list_filter，列表时，定制右侧快速筛选，可以组合筛选。

```
@admin.register(models.UserInfo)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'pwd', 'xxxxx')
    list_filter=('pub_date','title')
```

4. list_select_related，列表时，连表查询是否自动select_related。

5. list_editable，列表时，可以编辑的列 。

```
@admin.register(models.UserInfo)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'pub_date') 
    list_editable=('price',)
```

![img](https://images2017.cnblogs.com/blog/1000418/201801/1000418-20180126092825678-1667172063.png)

6. search_fields，列表时，模糊搜索的功能。

```
@admin.register(models.UserInfo)
class UserAdmin(admin.ModelAdmin):
    search_fields = ('user', 'pwd')
    会在页面产生一个搜索框，搜索的字段为user,pwd字段，可以模糊匹配
```

7. date_hierarchy，列表时，对Date和DateTime类型进行搜索。

```
@admin.register(models.UserInfo)
class UserAdmin(admin.ModelAdmin):
    date_hierarchy = 'ctime'
```

8  inlines，详细页面，如果有其他表和当前表做FK，那么详细页面可以进行动态增加和删除。

```
class BookInline(admin.StackedInline):
    extra = 0
    model = Book  # 书籍 的表

class PublishAdmin(admin.ModelAdmin):
    list_display=("name",)
    inlines =[BookInline,] # 关联 书籍，要创建在一上面，才能创建更多的书籍
```

![img](https://images2017.cnblogs.com/blog/1000418/201801/1000418-20180126093828694-1671095600.png)

9 action，列表时，定制action中的操作。

```
@admin.register(models.UserInfo)
class UserAdmin(admin.ModelAdmin):
 
    # 定制Action行为具体方法
    def func(self, request, queryset):
        print(self, request, queryset)
        print(request.POST.getlist('_selected_action'))
 
    func.short_description = "中文显示自定义Actions"
    actions = [func, ]
 
    # Action选项都是在页面上方显示
    actions_on_top = True
    # Action选项都是在页面下方显示
    actions_on_bottom = False
 
    # 是否显示选择个数
    actions_selection_counter = True
```

![img](https://images2017.cnblogs.com/blog/1000418/201801/1000418-20180126094138178-523357847.png)

10 定制HTML模板.

```
add_form_template = None
change_form_template = None
change_list_template = None
delete_confirmation_template = None
delete_selected_confirmation_template = None
object_history_template = None
```

```
change_list_template = "my_change_list.html"
```

```
{% extends "admin/base_site.html" %}
{% load i18n admin_urls static admin_list %}

{% block extrastyle %}

    <h1>yuAN</h1>
    
    
  {{ block.super }}
  <link rel="stylesheet" type="text/css" href="{% static "admin/css/changelists.css" %}" />
  {% if cl.formset %}
    <link rel="stylesheet" type="text/css" href="{% static "admin/css/forms.css" %}" />
  {% endif %}
  {% if cl.formset or action_form %}
    <script type="text/javascript" src="{% url 'admin:jsi18n' %}"></script>
  {% endif %}
  {{ media.css }}
  {% if not actions_on_top and not actions_on_bottom %}
    <style>
      #changelist table thead th:first-child {width: inherit}
    </style>
  {% endif %}
{% endblock %}

{% block extrahead %}
{{ block.super }}
{{ media.js }}
{% endblock %}

{% block bodyclass %}{{ block.super }} app-{{ opts.app_label }} model-{{ opts.model_name }} change-list{% endblock %}

{% if not is_popup %}
{% block breadcrumbs %}
<div class="breadcrumbs">
<a href="{% url 'admin:index' %}">{% trans 'Home' %}</a>
&rsaquo; <a href="{% url 'admin:app_list' app_label=cl.opts.app_label %}">{{ cl.opts.app_config.verbose_name }}</a>
&rsaquo; {{ cl.opts.verbose_name_plural|capfirst }}
</div>
{% endblock %}
{% endif %}

{% block coltype %}flex{% endblock %}

{% block content %}
  <div id="content-main">
    {% block object-tools %}
        <ul class="object-tools">
          {% block object-tools-items %}
            {% if has_add_permission %}
            <li>
              {% url cl.opts|admin_urlname:'add' as add_url %}
              <a href="{% add_preserved_filters add_url is_popup to_field %}" class="addlink">
                {% blocktrans with cl.opts.verbose_name as name %}Add {{ name }}{% endblocktrans %}
              </a>
            </li>
            {% endif %}
          {% endblock %}
        </ul>
    {% endblock %}
    {% if cl.formset.errors %}
        <p class="errornote">
        {% if cl.formset.total_error_count == 1 %}{% trans "Please correct the error below." %}{% else %}{% trans "Please correct the errors below." %}{% endif %}
        </p>
        {{ cl.formset.non_form_errors }}
    {% endif %}
    <div class="module{% if cl.has_filters %} filtered{% endif %}" id="changelist">
      {% block search %}{% search_form cl %}{% endblock %}
      {% block date_hierarchy %}{% date_hierarchy cl %}{% endblock %}

      {% block filters %}
        {% if cl.has_filters %}
          <div id="changelist-filter">
            <h2>{% trans 'Filter' %}</h2>
            {% for spec in cl.filter_specs %}{% admin_list_filter cl spec %}{% endfor %}
          </div>
        {% endif %}
      {% endblock %}

      <form id="changelist-form" method="post"{% if cl.formset.is_multipart %} enctype="multipart/form-data"{% endif %} novalidate>{% csrf_token %}
      {% if cl.formset %}
        <div>{{ cl.formset.management_form }}</div>
      {% endif %}

      {% block result_list %}
          {% if action_form and actions_on_top and cl.show_admin_actions %}{% admin_actions %}{% endif %}
          {% result_list cl %}
          {% if action_form and actions_on_bottom and cl.show_admin_actions %}{% admin_actions %}{% endif %}
      {% endblock %}
      {% block pagination %}{% pagination cl %}{% endblock %}
      </form>
    </div>
  </div>
{% endblock %}
```

11 raw_id_fields，详细页面，针对FK和M2M字段变成以Input框形式

```
@admin.register(models.UserInfo)
class UserAdmin(admin.ModelAdmin):
    raw_id_fields = ('FK字段', 'M2M字段',)
```

12  fields，详细页面时，显示字段的字段

```
@admin.register(models.UserInfo)
class UserAdmin(admin.ModelAdmin):
    fields = ('user',)
```

13 exclude，详细页面时，排除的字段

```
@admin.register(models.UserInfo)
class UserAdmin(admin.ModelAdmin):
    exclude = ('user',)
```

14  readonly_fields，详细页面时，只读字段

```
@admin.register(models.UserInfo)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)
```

15 fieldsets，详细页面时，使用fieldsets标签对数据进行分割显示

```
@admin.register(models.UserInfo)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ('基本数据', {
            'fields': ('user', 'pwd', 'ctime',)
        }),
        ('其他', {
            'classes': ('collapse', 'wide', 'extrapretty'),  # 'collapse','wide', 'extrapretty'
            'fields': ('user', 'pwd'),
        }),
    )
```

![img](https://images2017.cnblogs.com/blog/1000418/201801/1000418-20180126094917397-97501405.png)

 16 详细页面时，M2M显示时，数据移动选择（方向：上下和左右）

```
@admin.register(models.UserInfo)
class UserAdmin(admin.ModelAdmin):
    filter_vertical = ("m2m字段",) # 或filter_horizontal = ("m2m字段",)
```

![img](https://images2017.cnblogs.com/blog/1000418/201801/1000418-20180126095008865-1909980813.png)

17 ordering，列表时，数据排序规则

```
@admin.register(models.UserInfo)
class UserAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    或
    def get_ordering(self, request):
        return ['-id', ]
```

18. radio_fields，详细页面时，使用radio显示选项（FK默认使用select）

```
@admin.register(models.UserInfo)
class UserAdmin(admin.ModelAdmin):
    radio_fields = {'publish':admin.VERTICAL}
```

![img](https://images2017.cnblogs.com/blog/1000418/201801/1000418-20180126095306147-1362433976.png)

 19 form = ModelForm，用于定制用户请求时候表单验证，默认都是英文的错误

```
class myform(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        error_messages = {
            'title':{'required':'不能为空　'}
        }

class bookadmin(admin.ModelAdmin):
    list_display =  ('title','price','pub_date',)

form = myform

admin.site.register(Book,bookadmin)
```

20 empty_value_display = "列数据为空时，显示默认值"

```
@admin.register(models.UserInfo)
class UserAdmin(admin.ModelAdmin):
    empty_value_display = "列数据为空时，默认显示"
 
    list_display = ('user','pwd','up')
 
    def up(self,obj):
        return obj.user
    up.empty_value_display = "指定列数据为空时，默认显示"
```

## 2 admin源码解析

**1 单例模式**

**单例模式（Singleton Pattern）**是一种常用的软件设计模式，该模式的主要目的是确保**某一个类只有一个实例存在**。当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。

比如，某个服务器程序的配置信息存放在一个文件中，客户端通过一个 AppConfig 的类来读取配置文件的信息。如果在程序运行期间，有很多地方都需要使用配置文件的内容，也就是说，很多地方都需要创建 AppConfig 对象的实例，这就导致系统中存在多个 AppConfig 的实例对象，而这样会严重浪费内存资源，尤其是在配置文件内容很多的情况下。事实上，类似 AppConfig 这样的类，我们希望在程序运行期间只存在一个实例对象。

在 Python 中，我们可以用多种方法来实现单例模式：

- 使用模块
- 使用 `__new__`
- 使用装饰器（decorator）
- 使用元类（metaclass）

1.1 使用模块

其实，**Python 的模块就是天然的单例模式**，因为模块在第一次导入时，会生成 `.pyc` 文件，当第二次导入时，就会直接加载 `.pyc` 文件，而不会再次执行模块代码。因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。如果我们真的想要一个单例类，可以考虑这样做：

```
# mysingleton.py
class My_Singleton(object):
    def foo(self):
        pass
 
my_singleton = My_Singleton()
```

将上面的代码保存在文件 `mysingleton.py` 中，然后这样使用：

```
from mysingleton import my_singleton
my_singleton.foo()
```

1.2 使用__new__方法

为了使类只能出现一个实例，我们可以使用 `__new__` 来控制实例的创建过程，代码如下：

```
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)  
        return cls._instance  

class MyClass(Singleton):  
    a = 1
```

在上面的代码中，我们将类的实例和一个类变量 `_instance` 关联起来，如果 `cls._instance` 为 None 则创建实例，否则直接返回 `cls._instance`。

执行情况如下：

```
>>> one = MyClass()
>>> two = MyClass()
>>> one == two
True
>>> one is two
True
>>> id(one), id(two)
(4303862608, 4303862608)
```

 补充，静态方法，类方法（也可以创建单例模式）

```
class Foo(object):
    _instance = None  # 类属性

    def __init__(self, name):
        self.name = name

    @classmethod     # 类方法   cls == foo
    def instance(cls, *args, **kwargs):
        if not cls._instance:    # 如果为空
            obj = cls(*args, **kwargs)   # 实例化
            cls._instance = obj  # 赋予类属性
        return Foo._instance # _instance == cls(*args, **kwargs) == foo(*args,**kwargs) == 就是自己

    @staticmethod    # 静态方法
    def static(name):
        print(name)
        return name


# 单例模式，因为类属性在编译的时候会加载到内存 (类属性构造)
# obj1 = Foo.instance('alex')
# obj2 = Foo.instance('alex')
# print(id(obj1), id(obj2))


# 静态方法
# Foo.static('alex')  # 静态方法脱离类，外部可以直接通过类调用，不需要实例化，传参也跟类没有关系，相当于普通函数
# obj = Foo('egon')   # 实例化
# print(obj.static('alex'))   # 通过实例化调用，再给个参数，这样显得不论不类



class Singleton(object):
    _instance = None  # 类属性
    def __new__(cls, *args, **kwargs):
        if not cls._instance:  # 如果为None
            cls._instance = super(Singleton, cls).__new__(cls, *args ,**kwargs)    # Singleton 父类，cls子类__(cls,*args,**kwargs)
        return cls._instance
    
# 单例模式，同上面相同（new方法）
# ret1 = Singleton()
# print(ret1._instance)  # <__main__.Singleton object at 0x1023089e8>
# ret2 = Singleton()
# print(ret2._instance)
```

1.3 使用装饰器

我们知道，装饰器（decorator）可以动态地修改一个类或函数的功能。这里，我们也可以使用装饰器来装饰某个类，使其只能生成一个实例，代码如下：

```
from functools import wraps

def singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

@singleton
class MyClass(object):
    a = 1
```

在上面，我们定义了一个装饰器 `singleton`，它返回了一个内部函数 `getinstance`，该函数会判断某个类是否在字典 `instances` 中，如果不存在，则会将 `cls` 作为 key，`cls(*args, **kw)` 作为 value 存到 `instances` 中，否则，直接返回 `instances[cls]`。

1.4 使用metaclass

元类（metaclass）可以控制类的创建过程，它主要做三件事：

- 拦截类的创建
- 修改类的定义
- 返回修改后的类

使用元类实现单例模式的代码如下：

```
class Singleton(type):
    def __init__(self,name,bases,class_dict):
        super(Singleton,self).__init__(name,bases,class_dict)
        self._instance=None
    def __call__(self,*args,**kwargs):
        if self._instance is None:
            self._instance=super(Singleton,self).__call__(*args,**kwargs)
        return self._instance
if __name__=='__main__':
    class A(object):
        __metaclass__=Singleton      
    a=A()
    b=A()
    print id(a),id(b)
```

id是相同的。

例子中我们构造了一个Singleton元类，并使用__call__方法使其能够模拟函数的行为。构造类A时，将其元类设为Singleton，那么创建类对象A时，行为发生如下：

A=Singleton(name,bases,class_dict),A其实为Singleton类的一个实例。

创建A的实例时，A()=Singleton(name,bases,class_dict)()=Singleton(name,bases,class_dict).__call__()，这样就将A的所有实例都指向了A的属性_instance上，这种方法与方法1其实是相同的。

## 3 admin执行流程

1. 循环加载执行所有已经注册的app中的admin.py文件，点击admin源码可以看到如下函数，记得必须在settings里面注册项目

```
def autodiscover():
    autodiscover_modules('admin', register_to=site)
```

2. 执行代码，检测到注册，就要执行代码

```
＃admin.py
class BookAdmin(admin.ModelAdmin):
    list_display = ("title",'publishDate', 'price')
admin.site.register(Book, BookAdmin) 
admin.site.register(Publish)
```

3. admin.site  

![img](https://images2017.cnblogs.com/blog/1000418/201801/1000418-20180126102119725-160984558.png)

这里应用的是一个单例模式，对于AdminSite类的一个单例模式，执行的每一个app中的每一个admin.site都是一个对象

4 执行register方法，点击register里面看到如下代码

```
admin.site.register(Book, BookAdmin) 
admin.site.register(Publish)
```

```
class ModelAdmin(BaseModelAdmin):pass

def register(self, model_or_iterable, admin_class=None, **options):
　　self._registry={}
   if not admin_class:
           admin_class = ModelAdmin
   # Instantiate the admin class to save in the registry
   self._registry[model] = admin_class(model, self) # self就是admin.site，admin.site._registry[book]=ModelAdmin(book,)增加了简直对
　　如果注册的为多个，就会往字典里面加，一个表对象一个值，为了这个对象增加了样式，样式为这个value
```

思考：在每一个app的admin .py中加上

```
print(admin.site._registry)   ＃ 执行结果？单例模式，产生一个对象
```

5 admin的URL配置，点击site可以看到get_urls函数

```
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
```

```
class AdminSite(object):
    
     def get_urls(self):
        from django.conf.urls import url, include
      
        urlpatterns = []

        # Add in each model's views, and create a list of valid URLS for the
        # app_index
        valid_app_labels = []
        for model, model_admin in self._registry.items():
            urlpatterns += [
                url(r'^%s/%s/' % (model._meta.app_label, model._meta.model_name), include(model_admin.urls)),
            ]
            if model._meta.app_label not in valid_app_labels:
                valid_app_labels.append(model._meta.app_label)

        return urlpatterns

    @property
    def urls(self):
        return self.get_urls(), 'admin', self.name
```

6 url()方法的扩展应用，

```
from django.shortcuts import HttpResponse
def test01(request):
    return HttpResponse("test01")

def test02(request):
    return HttpResponse("test02")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^yuan/', ([
                    url(r'^test01/', test01),
                    url(r'^test02/', test02),

                    ],None,None)),

]
```

扩展优化

```
from django.conf.urls import url,include
from django.contrib import admin

from django.shortcuts import HttpResponse

def change_list_view(request):
    return HttpResponse("change_list_view")
def add_view(request):
    return HttpResponse("add_view")
def delete_view(request):
    return HttpResponse("delete_view")
def change_view(request):
    return HttpResponse("change_view")

def get_urls():

    temp=[
        url(r"^$".format(app_name,model_name),change_list_view),
        url(r"^add/$".format(app_name,model_name),add_view),
        url(r"^\d+/del/$".format(app_name,model_name),delete_view),
        url(r"^\d+/change/$".format(app_name,model_name),change_view),
    ]

    return temp


url_list=[]

for model_class,obj in admin.site._registry.items():

    model_name=model_class._meta.model_name     ### model对象名字
    app_name=model_class._meta.app_label　　　　　## 项目名称

    # temp=url(r"{0}/{1}/".format(app_name,model_name),(get_urls(),None,None))
    temp=url(r"{0}/{1}/".format(app_name,model_name),include(get_urls()))
    url_list.append(temp)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^yuan/', (url_list,None,None)),
]
```



转自：https://www.cnblogs.com/jokerbj/p/8358364.html

