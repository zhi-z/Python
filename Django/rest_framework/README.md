# REST framework简介

## 1 为什么要使用？

因为Django 包含了前段和后端两个部分，如果在开发的过程中不进行分离的话，一个人就需要写两个部分，前段和后端都需要写，这样感觉开发很不友好，所以引入了REST framework框架，把前段和后端进行分离，提高开发的效率，有时候开发一个应用，可能包括PC端和移动端，这样进行分离，能够保证只需要一个数据源就可以实现，而不需要进行另外的修改。

## 2 CBV

CBV中，在路由进行匹配的时候，首先调用的是父类中的as_view()函数，然后调用view函数，接着调用dispatch函数，其实在这个过程中主要的是调用dispatch函数，通过getattr来映射，然后执行该类中的函数。如果直接把dispatch 函数直接放在该类中，就会先执行该类中的dispatch函数，而不执行父类中的dispatch函数。

在源码中view的执行想相当于dispatch的执行，如果是get请求，则相当于执行self.get

![1540266626132](image\cbv.png)

## 3 REST framework使用

### 3.1 序列化类

**序列化理解：**

- 序列化（encoding)：把python对象编码转换成Json字符串。
- 反序列化（decoding）：把json格式字符串解码为python对象。 

> json库的主要方法：dumps, dump, loads, load 
>
> dumps功能 ： 将字典类型通过json把它序列化为json格式的字符串 
>
> loads功能 ：将json编码的字符串转换为python数据结构 

```
import json

dict = {'key1':'小蘑菇','key2':3,'key3':None,'key4':'summer'}

print('未序列化前的数据类型为',type(dict))
print('未序列化前的数据为:',dict)

str = json.dumps(dict)

print('序列化后的数据类型为',type(str))
print('序列化后的数据为:',str)

dict1 = json.loads(str)
print('反序列化后的数据类型为',type(dict1))
print('反序列化后的数据为:',dict1)
```



## 参考文献

<https://www.cnblogs.com/yuanchenqi/articles/8719520.html>

