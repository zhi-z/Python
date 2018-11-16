# jango数据库操作-增删改查-多对多关系以及一对多(外键)关系

### 一、一对多（外键）

例子：一个作者对应多本书，一本书只有一个作者，多的一边放外键

model代码：

```
class Person(models.Model);
name = models.CharField('作者姓名', max_length=10)
age = models.IntegerField('作者年龄')
 
class Book(models.Model):
person = models.ForeignKey(Person, related_name='person_book')
title = models.CharField('书籍名称', max_length=10)
pubtime = models.DateField('出版时间')

```

（一）获取对象方法： 

1.从作者出发获取书籍 

```
person = Person.objects.fiter(你的条件)
book = person.book_set.all()
```

2.从书籍出发获取作者 

```
p = book.person 
```

### 二、多对多

例子：一个作者对应多本书，一本书有多个作者

model代码：

```
class Author(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=40)  
    email = models.EmailField()  
      
class Book(models.Model):  
    title = models.CharField(max_length=200)  
    authors = models.ManyToManyField(Author)  
```

（一）获取对象方法： 

1.从书籍出发获取作者 

```
b = Book.objects.get(id=50)
b.authors.all()
b.authors.filter(first_name='Adam')
```

2.从作者出发获取书籍 

```
a = Author.objects.get(id=1)
a.book_set.all()
```

（二）添加对象方法： 

```
a = Author.objects.get(id=1)
b = Book.objects.get(id=50)
b.authors.add(a)
```

（三）删除对象对象方法： 

```
a = Author.objects.get(id=1)
b = Book.objects.get(id=50)
b.authors.remove(a) 或者 b.authors.filter(id=1).delete()
```



参考：

https://blog.csdn.net/shangliuyan/article/details/7920037

