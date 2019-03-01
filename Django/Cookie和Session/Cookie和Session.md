# Cookie和Session

`http` 协议是无状态的，意思是无记忆性的，如果需要保持用户名这种登录状态等情况，需要对用户的状态进行保存，这时就需要用到`cookie`和`session`了。

## 1 cookie

- `cookie`是由服务器生成，存储在浏览器端的一小段文本信息。 常用于记住用户名

> 特点：
>
> - 以键值对方式进行存储。
> - 通过浏览器访问一个网站时，会将浏览器存储的跟网站相关的所有`cookie`信息发送给该网站的服务器。request.COOKIES
> - `cookie`是基于域名安全的。
> -  `cookie`是有过期时间的，如果不指定，默认关闭浏览器之后cookie就会过期。

`cookie` 执行的过程如下图所示：

![](https://raw.githubusercontent.com/zhi-z/Python/master/Django/Cookie%E5%92%8CSession/images/cookie.png)

### 1.1  设置cookie

- 打开booktest/views.py文件，创建视图cookie_set

```
def cookie_set(request):
    response.set_cookie('h1', '你好')   # 设置cookie
    return HttpResponse("设置Cookie成功")
```

- 打开booktest/urls.py文件，配置url

```
    url(r'^cookie_set/$',views.cookie_set),
```

- 在浏览器输入如下网址

```
http://127.0.0.1:8000/cookie_set/
```

在"开发者工具"中可以在响应头中查看到设置的Cookie信息

### 1.2 读取cookie

Cookie信息被包含在请求头中，使用request对象的COOKIES属性访问。

- 打开booktest/views.py文件，创建视图cookie_get

```
def cookie_get(request):
    response = HttpResponse("读取Cookie，数据如下：<br>")
    if 'h1' in request.COOKIES:
        response.write('<h1>' + request.COOKIES['h1'] + '</h1>')
    return response
```

- 打开booktest/urls.py文件，配置url

```
    url(r'^cookie_get/$',views.cookie_get),
```

- 在浏览器输入如下网址

```
http://127.0.0.1:8000/cookie_get/
```

- 打开“开发者工具”，在请求头中可以查看Cookie信息

## 2 session

- 对于敏感、重要的信息，建议要储在服务器端，不能存储在浏览器中，如用户名、余额、等级、验证码等信息。在服务器端进行状态保持的方案就是`Session`。

> `session`的特点：
> `session`是以键值对进行存储的。
> `session`依赖于cookie。唯一的标识码保存在sessionid cookie中。
> `session`也是有过期时间，如果不指定，默认两周就会过期。-

- session执行的过程如下图所示：

![session](https://raw.githubusercontent.com/zhi-z/Python/master/Django/Cookie%E5%92%8CSession/images/session.png)

在使用Session后，会在Cookie中存储一个sessionid的数据，每次请求时浏览器都会将这个数据发给服务器，服务器在接收到sessionid后，会根据这个值找出这个请求者的Session。如果想使用Session，浏览器必须支持Cookie，否则就无法使用Session了。存储Session时，键与Cookie中的sessionid相同，值是开发人员设置的键值对信息，进行了base64编码，过期时间由开发人员设置。

- Django项目默认启用Session，在settings.py文件，在项MIDDLEWARE中启用Session中间件，如图所示：

![](https://raw.githubusercontent.com/zhi-z/Python/master/Django/Cookie%E5%92%8CSession/images/session_middleware.png)

### 2.1 存储方式 

打开settings.py文件，设置`SESSION_ENGINE`项指定`Session`数据存储的方式，可以存储在数据库、缓存、Redis等。

- 存储在数据库中，如下设置可以写，也可以不写，这是默认存储方式

```
SESSION_ENGINE='django.contrib.sessions.backends.db'
```

- 存储在缓存中：存储在本机内存中，如果丢失则不能找回，比数据库的方式读写更快

```
SESSION_ENGINE='django.contrib.sessions.backends.cache'
```

- 混合存储：优先从本机内存中存取，如果没有则从数据库中存取。

```
SESSION_ENGINE='django.contrib.sessions.backends.cached_db'
```

- 如果存储在数据库中，需要在项`INSTALLED_APPS`中安装`Session`应用，迁移后会在数据库中创建出存储Session的表 ，如图所示：

![](https://raw.githubusercontent.com/zhi-z/Python/master/Django/Cookie%E5%92%8CSession/images/session_table.png)





### 2.2 session 操作

##### 对象及方法

通过HttpRequest对象的session属性进行会话的读写操作

1. 以键值对的格式写session。

```
request.session['键']=值
```

2. 根据键读取值

```
request.session.get('键',默认值)
```

2. 清除所有session，在存储中删除值部分

```
request.session.clear()
```

3. 清除session数据，在存储中删除session的整条数据

```
request.session.flush()
```

4. 删除session中的指定键及值，在存储中只删除某个键及对应的值

```
del request.session['键']
```

5. 设置会话的超时时间，如果没有指定过期时间则两个星期后过期

```
request.session.set_expiry(value)
```

- 如果value是一个整数，会话将在value秒没有活动后过期。
- 如果value为0，那么用户会话的Cookie将在用户的浏览器关闭时过期。
- 如果value为None，那么会话永不过期

##### 使用

```
# /set_session
def set_session(request):
    '''设置session'''
    request.session['username'] = 'smart'
    request.session['age'] = 18
    # request.session.set_expiry(5)   # 设置有效时间
    return HttpResponse('设置session')


# /get_session
def get_session(request):
    '''获取session'''
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username+':'+str(age))

#　/clear_session
def clear_session(request):
    '''清除session信息'''
    # request.session.clear()
    request.session.flush()
    return HttpResponse('清除成功')
```

## 3 使用场景

- `cookie`:记住用户名。安全性要求不高。
- `session`:涉及到安全性要求比较高的数据。银行卡账户,密码