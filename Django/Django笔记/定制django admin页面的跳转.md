## [定制django admin页面的跳转](https://www.cnblogs.com/livingintruth/p/3738601.html)

在django admin的 change_view,  add_view和delete_view页面,如果想让页面完成操作后跳转到我们想去的url,该怎么做

默认django admin会跳转到changelist_view页面

下面的代码是django1.6的



下面是一个可行的做法,写admin model的时候重写父类admin.ModelAdmin的change_view 方法

```
from django.contrib import admin
class MyAdmin(admin.ModelAdmin):
    def change_view(self, request, object_id, form_url='', extra_context=None):
        result_template = super(MyAdmin, self).change_view(request, object_id, form_url, extra_context)
        result_template['location'] = '/dest/url'
        return result_template           
```

可以看到,就是调用ModelAdmin的change_view得到结果,然后给 result_template做了一个这个操作

```
 result_template['location'] = '/dest/url'
```

然后返回

 

为什么这样可行? 我们看看发生了什么

 

我们重写change_view,当然参数必须和父类一样了

 

首先调用了父类ModelAdmin.change_view的这个函数,这个函数返回了什么呢

追溯一下源代码,它返回的是一个TemplateResponse对象, 是通过调用 ModelAdmin.render_change_form()

 

```
return TemplateResponse(request, form_template or [
    "admin/%s/%s/change_form.html" % (app_label, opts.model_name), 
    "admin/%s/change_form.html" % app_label,
    "admin/change_form.html"        
 ], context, current_app=self.admin_site.name)     
```

 

那么接下来我们看看TemplateResponse

 其实有这样的派生关系: TemplateResponse <----  SimpleTemplage  <-----HttpRespone  <--- HttpResponseBase

 

HttpResponse里实现了 

```
def __setitem__(self, header, value):
    header = self._convert_to_charset(header, 'ascii')
    value = self._convert_to_charset(value, 'latin-1', mime_encode=True)
    self._headers[header.lower()] = (header, value)
```

 

而如果一个类实现了 __setitem__,  那么[] 操作符就会去调用这个函数(相当于C++中的重载)

```
result_template['location'] = '/dest/url'
```

 

所以上面这行代码就在服务器返回的Response的header中写入了location, 而浏览器收到的Http Response的header中如果有location,就会跳转到location指定的 url

 

\-------------------------------------------------------

 

但是我还发现了一个现象, 当进入到一个model item的change_view界面时,也就是GET请求这个url,虽然服务端返回了location,但是浏览器没有跳转,可能是因为当前有form需要提交.

 而在change_view界面修改完后, 点击提交表单,浏览器收到服务端的location后,就发生了跳转.