# Ubuntu pytho2与python3版本切换

## 1 切换**Python3**为默认版本

```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 100
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 150
```

## 2 切换**Python2**为默认版本

```
sudo update-alternatives --config python
```

## 3 查看版本

```
python --version
```

## 4 切换之后不用用pip3问题

在从python2切换到python3 后有时候pip还是使用pip2 ，所以要切换到pip3,使用如下方法：

https://blog.csdn.net/qq_15067531/article/details/77841780