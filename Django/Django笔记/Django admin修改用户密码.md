# Django admin修改用户密码

如果忘记了django的admin的密码，而数据库中的auth_user中关于密码的字段是经过加密的，这个时候你就可以通过django的命令来直接修改admin的密码

## 1 方法一

 这个方法是用过shell命令方式对密码进行修改的，使用如下的命令：

```
python manage.py shell  

from django.contrib.auth.models import User

user =User.objects.get(username='admin')

user.set_password('new_password')  

user.save()
```

这样就完成了密码的修改。

## 2 方法二

这个方法是直接创建新的用户。使用如下命令。

```
 python manage.py changepassword 
```

接着输入用户名和密码，就可以完成新用户的创建

