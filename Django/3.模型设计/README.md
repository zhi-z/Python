# Django模型设计

操作数据库是通过写sql语句，那么能不能不写sql语句就可以操作数据库呢？ 可以，就是通过接下来要给大家讲的**ORM框架**。

## 1 ORM框架

O是object，也就**类对象**的意思，R是relation，翻译成中文是关系，也就是关系数据库中**数据表**的意思，M是mapping，是**映射**的意思。在ORM框架中，它帮我们把类和数据表进行了一个映射，可以让我们**通过类和类对象就能操作它所对应的表格中的数据**。ORM框架还有一个功能，它可以**根据我们设计的类自动帮我们生成数据库中的表格**，省去了我们自己建表的过程。

django中内嵌了ORM框架，不需要直接面向数据库编程，而是定义模型类，通过模型类和对象完成数据表的增删改查操作。如图所示。

![](E:\GitHub\Python\Django\3.模型设计\image\orm.png)

## 2 Django数据库开发步骤

使用django进行数据库开发的步骤如下：

- 1.在models.py中定义模型类
- 2.迁移
- 3.通过类和对象完成数据增删改查操作

下面我们以保存图书信息为例来给大家介绍Django中进行数据库开发的整个流程。

### 2.1 定义模型类

模型类定义在models.py文件中，继承自models.Model类。

> 说明：不需要定义主键列，在生成时会自动添加，并且值为自动增长。

#### 设计图书类

图书类：

- 类名：BookInfo
- 图书名称：btitle
- 图书发布日期：bpub_date

#### 模型类的设计

根据设计，在models.py中定义模型类如下：

```
from django.db import models

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
```

### 2.2 迁移

迁移前目录结构如下图：

![迁移前](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_1.png)

迁移由两步完成:

- 1.生成迁移文件：根据模型类生成创建表的迁移文件。
- 2.执行迁移：根据第一步生成的迁移文件在数据库中创建表。

生成迁移文件命令如下：

```
python manage.py makemigrations
```

![生成迁移文件](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_2.png)

执行生成迁移文件命令后，会在应用booktest目录下的migrations目录中生成迁移文件。

生成迁移文件后的目录结构： ![生成迁移文件后](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_13.png)

打开上图中的迁移文件，内容如下： ![迁移文件](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_14.png)

Django框架根据我们设计的模型类生成了迁移文件，在迁移文件中我们可以看到fields列表中每一个元素跟BookInfo类属性名以及属性的类型是一致的。同时我们发现多了一个id项，这一项是Django框架帮我们自动生成的，在创建表的时候id就会作为对应表的主键列，并且主键列自动增长。

执行迁移命令如下：

```
python manage.py migrate
```

![执行迁移](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_3.png)

当执行迁移命令后，Django框架会读取迁移文件自动帮我们在数据库中生成对应的表格。

迁移后目录结构如下图：

![迁移后](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_4.png)

Django默认采用sqlite3数据库，上图中的db.sqlite3就是Django框架帮我们自动生成的数据库文件。 sqlite3是一个很小的数据库，通常用在手机中，它跟mysql一样，我们也可以通过sql语句来操作它。

下面使用sqliteman打开db.sqlite3文件进行查看。如果没有安装sqliteman，需要先使用如下命令进行安装。

```
sudo apt-get install sqliteman
```

安装成功之后，在终端输入sqliteman命令，敲击回车即可打开软件。

sqliteman界面如下： ![sqliteman界面](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_15.png)

按照下图的步骤找到要打开的数据库文件。

![打开数据库](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_16.png)

点击打开之后，点开Tables找到booktest_bookinfo，可以发现这个表中有三个列，列名跟BookInfo中类属性的名字是一样的。

![表界面](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_17.png)

双击上图中的booktest_bookinfo表，可以在右侧的Full View窗口中查看表格中的数据，这里表中还没有数据。

![查看表数据](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_18.png)

#### 默认生成的表名称

上面生成的表的名字叫做booktest_bookinfo，booktest是应用的名字，bookinfo是模型类的名字。

数据表的默认名称为：

```
<app_name>_<model_name>
例：
booktest_bookinfo
```

#### 设计英雄类

英雄类：

- 类名：HeroInfo
- 英雄姓名：hname
- 英雄性别：hgender
- 英雄简介：hcomment
- 英雄所属图书：hbook
- 图书-英雄的关系为一对多

打开booktest/models.py，定义英雄类代码如下：

```
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcomment = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo')
```

这里要说明的是，BookInfo类和HeroInfo类之间具有一对多的关系，这个一对多的关系应该定义在多的那个类，也就是HeroInfo类中。

> hbook = models.ForeignKey('BookInfo')这句代码就让BookInfo类和HeroInfo类之间建立了一对多的关系。

**在我们之后迁移生成表的时候，Django框架就会自动帮我们在图书表和英雄表之间建立一个外键关系。**

生成迁移文件：

```
python manage.py makemigrations
```

结果如下图：

![生成迁移文件](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_19.png)

项目目录结构：

![项目目录结构](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_20.png)

执行迁移的命令：

```
python manage.py migrate
```

![执行迁移](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_21.png)

最后我们可以看到数据库中生成的英雄表如下图：

![英雄表](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_22.png)

注意上图中booktest_heroinfo表中有一列hbook_id，这一列名为什么不叫hbook？ hbook_id是根据HeroInfo类的关系属性hbook生成的，对应着图书表中的主键id。

### 2.3 数据操作

完成数据表的迁移之后，下面就可以通过进入项目的shell，进行简单的API操作。如果需要退出项目，可以使用ctrl+d快捷键或输入quit()。

进入项目shell的命令：

```
python manage.py shell
```

![shell](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_5.png)

首先引入booktest/models中的类：

```
from booktest.models import BookInfo,HeroInfo
```

查询所有图书信息：

```
BookInfo.objects.all()
```

因为当前并没有数据，所以返回空列表

![查询](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_6.png)

新建图书对象：

```
b=BookInfo()
b.btitle="射雕英雄传"
from datetime import date
b.bpub_date=date(1991,1,31)
b.save()
```

![添加](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_7.png)

再次查询所有图书信息：

```
BookInfo.objects.all()
```

![查询2](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_8.png)

查找图书信息并查看值：

```
b=BookInfo.objects.get(id=1)
b
b.id
b.btitle
b.bpub_date
```

![查找](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_9.png)

修改图书信息：

```
b.bpub_date=date(2017,1,1)
b.save()
b.bpub_date
```

![修改](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_10.png)

删除图书信息：

```
b.delete()
```

![删除](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_11.png)

#### 对象的关联操作

对于HeroInfo可以按照上面的方式进行增删改查操作。

创建一个BookInfo对象

```
b=BookInfo()
b.btitle='abc'
b.bpub_date=date(2017,1,1)
b.save()
```

创建一个HeroInfo对象

```
h=HeroInfo()
h.hname='a1'
h.hgender=False
h.hcomment='he is a boy'
h.hbook=b
h.save()
```

图书与英雄是一对多的关系，django中提供了关联的操作方式。

获得关联集合：返回当前book对象的所有hero。

```
b.heroinfo_set.all()
```

![关联集合](https://raw.githubusercontent.com/zhi-z/Python/master/Django/3.%E6%A8%A1%E5%9E%8B%E8%AE%BE%E8%AE%A1/image/p3_12.png)