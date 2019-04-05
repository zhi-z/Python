# MySQL安装


ubuntu上安装mysql非常简单只需要几条命令就可以完成。

- sudo apt-get install mysql-server  # 安装MySQL服务
- sudo apt-get install mysql-client            # 安装客户端
  注意：安装过程中会提示设置密码什么的，注意设置了不要忘了，安装完成之后可以使用如下命令来检查是否安装成功：如图所示使用

```
sudo service mysql start    # 开启服务
ps ajx | grep mysql    
```
通过如上命令,如果有如下图的红框部分,那么就说明安装MySQL成功.
![在这里插入图片描述](image/start_sql.png)
 登陆mysql数据库可以通过如下命令：
    mysql -uroot -p密码

-u 表示选择登陆的用户名， -p 表示登陆的用户密码，上面命令输入之后会提示输入密码，此时输入密码就可以登录到mysql。
![](image/logn.png)
接着通过selct version()获取客户端版本信息，如上图所示。

创建用户和授权：

```
创建用户：
    create user 'hiram'@'192.168.1.1' identified by '123123';
    create user 'hiram'@'192.168.1.%' identified by '123123';
    create user 'hiram'@'%' identified by '123123';
授权：
	权限  人
        grant select,insert,update  on db1.t1 to 'hiram'@'%';
        grant all privileges  on db1.t1 to 'hiram'@'%';

        revoke all privileges on db1.t1 from 'hiram'@'%';
```


**参考文献：[Ubuntu 安装mysql和简单操作](https://www.cnblogs.com/zhuyp1015/p/3561470.html)**