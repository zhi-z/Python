# Django 重定向

在Django中，当我们向服务器请求时，服务器处理完毕后不是返回页面，而是告诉浏览器再去请求其他的url地址，这个过程叫页面重定向。过程如下图所示：

![](images\redirect.png)

在Django中使用HttpResponseRedirect('链接')函数或者redirect('链接')函数实现。