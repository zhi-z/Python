# Django自带的用户认证

我们在开发一个网站的时候，无可避免的需要设计实现网站的用户系统。此时我们需要实现包括用户注册、用户登录、用户认证、注销、修改密码等功能，这还真是个麻烦的事情呢。

Django作为一个完美主义者的终极框架，当然也会想到用户的这些痛点。它内置了强大的用户认证系统--auth，它默认使用 auth_user 表来存储用户数据。

## 1 auth模块

```
from django.contrib import auth
```

auth中提供了许多实用方法：

### 1.1 **authenticate()**   

提供了用户认证功能，即验证用户名以及密码是否正确，一般需要username 、password两个关键字参数。

如果认证成功（用户名和密码正确有效），便会返回一个 User 对象。

authenticate()会在该 User 对象上设置一个属性来标识后端已经认证了该用户，且该信息在后续的登录过程中是需要的。

用法：

```
user = authenticate(username='theuser',password='thepassword')
```

### 1.2 **login(HttpRequest, user)**　　

该函数接受一个HttpRequest对象，以及一个经过认证的User对象。

该函数实现一个用户登录的功能。它本质上会在后端为该用户生成相关session数据。

用法：

```
from django.contrib.auth import authenticate, login
   
def my_view(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(username=username, password=password)
  if user is not None:
    login(request, user)
    # Redirect to a success page.
    ...
  else:
    # Return an 'invalid login' error message.
    ...
```

### 1.3 **logout(request)** 

该函数接受一个HttpRequest对象，无返回值。

当调用该函数时，当前请求的session信息会全部清除。该用户即使没有登录，使用该函数也不会报错。

用法：

```
from django.contrib.auth import logout
   
def logout_view(request):
  logout(request)
  # Redirect to a success page.
```

### 1.4 is_authenticated()

用来判断当前请求是否通过了认证。

用法：

```
def my_view(request):
  if not request.user.is_authenticated():
    return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
```

### 1.5 **login_requierd()**

auth 给我们提供的一个装饰器工具，用来快捷的给某个视图添加登录校验。

用法：

```
from django.contrib.auth.decorators import login_required
      
@login_required
def my_view(request):
  ...
```

若用户没有登录，则会跳转到django默认的 登录URL '/accounts/login/ ' 并传递当前访问url的绝对路径 (登陆成功后，会重定向到该路径)。

如果需要自定义登录的URL，则需要在settings.py文件中通过LOGIN_URL进行修改。

示例：

```
LOGIN_URL = '/login/'  # 这里配置成你项目登录页面的路由
```

### 1.5 create_user()

auth 提供的一个创建新用户的方法，需要提供必要参数（username、password）等。

用法：

```
from django.contrib.auth.models import User
user = User.objects.create_user（username='用户名',password='密码',email='邮箱',...）
```

### 1.6 create_superuser()

auth 提供的一个创建新的超级用户的方法，需要提供必要参数（username、password）等。

用法：

```
from django.contrib.auth.models import User
user = User.objects.create_superuser（username='用户名',password='密码',email='邮箱',...）
```

### 1.7 check_password(password)

auth 提供的一个检查密码是否正确的方法，需要提供当前请求用户的密码。

密码正确返回True，否则返回False。

用法：

```
ok = user.check_password('密码')
```

### 1.8 set_password(password)

auth 提供的一个修改密码的方法，接收 要设置的新密码 作为参数。

注意：设置完一定要调用用户对象的save方法！！！

用法：

```
user.set_password(password='')
user.save()
```

**一个修改密码功能的简单示例**

```
@login_required
def set_password(request):
    user = request.user
    err_msg = ''
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '')
        new_password = request.POST.get('new_password', '')
        repeat_password = request.POST.get('repeat_password', '')
        # 检查旧密码是否正确
        if user.check_password(old_password):
            if not new_password:
                err_msg = '新密码不能为空'
            elif new_password != repeat_password:
                err_msg = '两次密码不一致'
            else:
                user.set_password(new_password)
                user.save()
                return redirect("/login/")
        else:
            err_msg = '原密码输入错误'
    content = {
        'err_msg': err_msg,
    }
    return render(request, 'set_password.html', content)
```

### 1.9 User对象的属性

User对象属性：username， password

is_staff ： 用户是否拥有网站的管理权限.

is_active ： 是否允许用户登录, 设置为 False，可以在不删除用户的前提下禁止用户登录。

## 2 扩展默认的auth_user表

这内置的认证系统这么好用，但是auth_user表字段都是固定的那几个，我在项目中没法拿来直接使用啊！

比如，我想要加一个存储用户手机号的字段，怎么办？

聪明的你可能会想到新建另外一张表然后通过一对一和内置的auth_user表关联，这样虽然能满足要求但是有没有更好的实现方式呢？

答案是当然有了。

我们可以通过继承内置的 AbstractUser 类，来定义一个自己的Model类。

这样既能根据项目需求灵活的设计用户表，又能使用Django强大的认证系统了。

```
from django.contrib.auth.models import AbstractUser
class UserInfo(AbstractUser):
    """
    用户信息表
    """
    nid = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11, null=True, unique=True)
    
    def __str__(self):
        return self.username
```

注意：

按上面的方式扩展了内置的auth_user表之后，一定要在settings.py中告诉Django，我现在使用我新定义的UserInfo表来做用户认证。写法如下：

```
# 引用Django自带的User表，继承使用时需要设置
AUTH_USER_MODEL = "app名.UserInfo"
```

再次注意：

一旦我们指定了新的认证系统所使用的表，我们就需要重新在数据库中创建该表，而不能继续使用原来默认的auth_user表了。



转自：[Django的认证系统](https://www.cnblogs.com/liwenzhou/p/9030211.html)