# Django MySQL配置

在进行配置之前需要先安装pymysql，否则后面配置完成后会运行不成功，安装pymysql命令如下：

```
pip install pymysql 
```

配置的步骤如下：

### 1 创建项目

```
# django-admin startproject 项目名称
django-admin startproject python_django
```

创建完成后项目的目录如下：

![](https://raw.githubusercontent.com/zhi-z/Python/master/Django/6.model%E5%90%8E%E7%AB%AF%E9%85%8D%E7%BD%AE/image/create_project.png)

### 2 配置

打开python_django/settings.py，默认使用的是sqlite3数据库，如图所示

![](https://raw.githubusercontent.com/zhi-z/Python/master/Django/6.model%E5%90%8E%E7%AB%AF%E9%85%8D%E7%BD%AE/image/default_settings.png)

修改为MySQL数据库，实现的代码如下：

> 将引擎改为mysql，提供连接的主机HOST、端口PORT、数据库名NAME、用户名USER、密码PASSWORD。 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_db', #数据库名字，
        'USER': 'root', #数据库登录用户名
        'PASSWORD': '123456', #数据库登录密码
        'HOST': 'localhost', #数据库所在主机
        'PORT': '3306', #数据库端口
    }
}
```

> 注意：数据库test_db Django框架不会自动生成，需要我们自己进入mysql数据库去创建。 

接着在python_django\_\_init\_\_.py中进行配置，需要加入如下两行代码：

> python_django\_\_init\_\_.py
>
> ```
> import pymysql
> pymysql.install_as_MySQLdb()
> ```



完成配置。