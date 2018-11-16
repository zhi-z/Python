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

