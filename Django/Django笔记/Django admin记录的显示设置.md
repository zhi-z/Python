# Django admin记录的显示设置

看django操作数据库的时候 有写

```
def __unicode__(self)
```

这么写的作用是什么啊？

这个__str__的作用是美化打印出来的结果，使人类更方便查看。看下面例子，如果没有__st__方法，打印的结果是<__main__.Test object at 0x0000022D6D1387B8>格式，有了__str__方法后，打印时会按照__str__定义的格式来打印，打印结果为Name:xiaoming。

```
class Test:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def __str__(self):
        return 'Name:' + self.name

instance = Test('xiaoming', 'Teacher')
print(instance)
```

在Django中，如果用的是Python3的话就只能用__str__方法，如果是Python2的话就使用__unicode__方法。因为更安全一些。