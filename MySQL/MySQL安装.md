# MySQL安装

ubuntu上安装mysql非常简单只需要几条命令就可以完成。

- sudo apt-get install mysql-server
- apt-get isntall mysql-client
- sudo apt-get install libmysqlclient-dev
  注意：安装过程中会提示设置密码什么的，注意设置了不要忘了，安装完成之后可以使用如下命令来检查是否安装成功：
  ` sudo netstat -tap | grep mysql`

通过上述命令检查之后，如果看到有mysql 的socket处于 listen 状态则表示安装成功。
 登陆mysql数据库可以通过如下命令：

    mysql -uroot -p密码

-u 表示选择登陆的用户名， -p 表示登陆的用户密码，上面命令输入之后会提示输入密码，此时输入密码就可以登录到mysql。
![](https://img-blog.csdn.net/20181012161656698?)
接着通过selct version()获取客户端版本信息，如上图所示。


**参考文献：[Ubuntu 安装mysql和简单操作](https://www.cnblogs.com/zhuyp1015/p/3561470.html)**