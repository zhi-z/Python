# Django 部署

经过一周的调试，永磁同步电机的后台数据终于打通了，也算是基本实现，后面还需要更加的完善，不过现在数据能够打通。在测试上基本实现以后，需要在服务器上进行部署，在Django使用WSGI作为python web的服务器 。部署的步骤也比较简单：

## 1 安装uWSGI

uWSGI实现了WSGI的所有接口，是一个快速、自我修复、开发人员和系统管理员友好的服务器。uWSGI代码完全用C编写，效率高、性能稳定。 

```
pip install uwsgi
```

## 2 配置uWSGI 

在项目目录下创建uwsgi.ini文件，配置如下：

```
[uwsgi]
#使用nginx连接时使用
#socket=127.0.0.1:8080
#直接做web服务器使用
http=0.0.0.0:1081
#项目目录
chdir=/home/datah/MyDocuments/django/pmsm-dev/NorthPMSM
#项目中wsgi.py文件的目录，相对于项目目录
wsgi-file=NorthPMSM/NorthPMSMwsgi.py
processes=4
threads=2
master=True
pidfile=uwsgi.pid
daemonize=uwsgi.log
# 虚拟环境的位置
virtualenv = /home/datah/MyDocuments/django/pmsm-dev/pmsm_env
```

##  3 常用命令

### 3.1 启动

```
uwsgi --ini uwsgi.ini
```

### 3.2 查看

```
ps ajx|grep uwsgi
```

### 3.3 停止

```
uwsgi --stop uwsgi.pid
```