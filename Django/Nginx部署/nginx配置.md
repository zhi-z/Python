# nginx配置

1.安装nginx:pip install nginx
2.启动：
          cd /usr/local/nginx/（或usr/local/）
          启动：sudo sbin/nginx（在sbin中运行sudo nginx）
3.查看进程：ps ajx|grep nginx
4.停止进程：sudo sbin/nginx -s stop（在sbin目录下运行nginx -s stop）
5.在浏览器上输入域名：

启动：

![1547452171354](images\1547452171354.png)



停止：

![1547452258465](images\1547452258465.png)



在浏览器上输入我们绑定的域名：

![1547452294906](images\1547452294906.png)

然后就可以使用sudo service nginx {start|stop|restart|reload|force-reload|status|configtest|rotate|upgrade}的命令启动。 