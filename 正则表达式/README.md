# 正则表达式

正则表达式是**处理字符串**的强大工具，拥有独特的语法和独立的处理引擎。

我们在大文本中匹配字符串时，有些情况用str自带的函数(比如find, in)可能可以完成，有些情况会稍稍复杂一些，这个时候我们需要一个某种模式的工具，这个时候**正则表达式**就派上用场了。

说起来正则表达式效率上可能不如str自带的方法，但匹配功能实在强大太多。

## 1 语法

当你要匹配 **一个/多个/任意个 数字/字母/非数字/非字母/某几个字符/任意字符**，想要 **贪婪/非贪婪** 匹配，想要捕获匹配出来的 **第一个/所有** 内容的时候，可以参考以下的小抄。

![](C:\Users\DataH\Desktop\GitHub\Python\正则表达式\image\positive_expression_syntax.jpg)

- 验证工具：https://regexr.com/
- 正则表达式练习：https://alf.nu/RegexGolf

## 2 Python案例

### 2.1 re 模块使用

- 基本流程
  - 导入re模块
  - 使用match方法进行匹配操作,result = re.match(正则表达式，要匹配的字符串)
  - 通group方法提取匹配的数据,result.group()
- 案例：

```python
import re
```

```python
# 满足正则表达式的就会有返回值，返回的是一个对象
result = re.match(r"hello","hello raindi")
```

```python
result.group()
```

```
'hello'
```

### 2.2 匹配单个字符

| 字符 | 功能                                   |
| ---- | -------------------------------------- |
| .    | 匹配任意1个字符（除了\n）              |
| [ ]  | 匹配[ ]中列举的字符                    |
| \d   | 匹配数字，即0-9                        |
| \D   | 匹配非数字，即不是数字                 |
| \s   | 匹配空白，即 空格，tab键               |
| \S   | 匹配非空白                             |
| \w   | 匹配单词字符，即a-z、A-Z、0-9、_、中文 |
| \W   | 匹配非单词字符                         |

In [1]:

```
import re
```

```
# 使用\d对数字进行匹配
result = re.match(r"班级：\d","班级：1")
```

```
result.group()
```

Out[5]:

```
'班级：1'
```

In [6]:

```
result = re.match(r"班级：\d","班级：2")
```

```
result.group()
```

Out[6]:

```
'班级：2'
```

In [7]:

```
result = re.match(r"班级：\d","班级：6")
```

```
result.group()  # 获取匹配的结果
```

Out[7]:

```
'班级：6'
```

- 通过以上实验：\d只能匹配0-9中的任意一个

In [9]:

```
re.match(r"班级：[1234567]","班级：5").group()
```

Out[9]:

```
'班级：5'
```

In [11]:

```
re.match(r"班级：[1234567]","班级：2").group()
```

Out[11]:

```
'班级：2'
```

In [16]:

```
re.match(r"班级：[1234567]","班级：8") 
# 没有结果返回
```

In [14]:

```
# 使用'-'来表示连续字符
re.match(r"班级：[1-5]","班级：8")  
# 没有返回结果
```

In [15]:

```
re.match(r"班级：[1-5]","班级：4")  
# 有结果返回
```

Out[15]:

```
<_sre.SRE_Match object; span=(0, 4), match='班级：4'>
```

In [17]:

```
re.match(r"班级：[1-47-9]","班级：4")  
# 有返回结果
```

Out[17]:

```
<_sre.SRE_Match object; span=(0, 4), match='班级：4'>
```

In [18]:

```
# 在[] 中只取1 2 3 4 7 8 9
re.match(r"班级：[1-47-9]","班级：5") 
# 没有返回结果 
```

In [19]:

```
# 对字符进行匹配
re.match(r"班级：[1-47-9abcd]","班级：a")
```

Out[19]:

```
<_sre.SRE_Match object; span=(0, 4), match='班级：a'>
```

In [20]:

```
# 匹配的范围0-9和所有的英文字母，包括大小写
re.match(r"班级：[0-9a-zA-Z]","班级：H")
```

Out[20]:

```
<_sre.SRE_Match object; span=(0, 4), match='班级：H'>
```

- 通过以上的实验：使用[...]可以匹配[]中的数据

In [21]:

```
# 使用\w匹配单个数字和单个英文字符（包括大小写）还有中文
re.match(r"班级：\w","班级：G")
```

Out[21]:

```
<_sre.SRE_Match object; span=(0, 4), match='班级：G'>
```

In [22]:

```
re.match(r"班级：\w","班级：6")
```

Out[22]:

```
<_sre.SRE_Match object; span=(0, 4), match='班级：6'>
```

In [23]:

```
# \w匹配中文
re.match(r"班级：\w","班级：二")
```

Out[23]:

```
<_sre.SRE_Match object; span=(0, 4), match='班级：二'>
```



### 2.3 匹配多个字符

| 字符  | 功能                                                |
| ----- | --------------------------------------------------- |
| *     | 匹配前一个字符出现0次或者无限次，即可有可无         |
| +     | 匹配前一个字符出现1次或者无限次，即至少有1次        |
| ?     | 匹配前一个字符出现1次或者0次，即要么有1次，要么没有 |
| {m}   | 匹配前一个字符出现m次                               |
| {m,n} | 匹配前一个字符出现从m到n次                          |



In [24]:

```
import re
```

In [25]:

```
# 使用{}匹配多个,1,2表示能匹配到1位到2位
re.match(r"班级：\d{1,2}","班级：2")
```

Out[25]:

```
<_sre.SRE_Match object; span=(0, 4), match='班级：2'>
```

In [26]:

```
re.match(r"班级：\d{1,2}","班级：22")
```

Out[26]:

```
<_sre.SRE_Match object; span=(0, 5), match='班级：22'>
```

In [27]:

```
# 使用{}匹配多个,1,4表示能匹配到1位到4位
re.match(r"班级：\d{1,4}","班级：2")
```

Out[27]:

```
<_sre.SRE_Match object; span=(0, 4), match='班级：2'>
```

In [28]:

```
re.match(r"班级：\d{1,4}","班级：234")
```

Out[28]:

```
<_sre.SRE_Match object; span=(0, 6), match='班级：234'>
```

In [29]:

```
re.match(r"班级：\d{1,4}","班级：2345")
```

Out[29]:

```
<_sre.SRE_Match object; span=(0, 7), match='班级：2345'>
```

In [43]:

```
# 使用{}匹配多个,匹配手机号码,只能有11位数字
re.match(r"手机号码:\d{11}","手机号码:15354286712").group()
```

Out[43]:

```
'手机号码:15354286712'
```

In [46]:

```
# 使用{}匹配多个,匹配带区号的电话号码，'?'使用
re.match(r"电话号码:076-?\d{7}","电话号码:076-7561235").group()
```

Out[46]:

```
'电话号码:076-7561235'
```

In [47]:

```
# 使用{}匹配多个,匹配带区号的电话号码
re.match(r"电话号码:076-?\d{7}","电话号码:0767561235").group()
```

Out[47]:

```
'电话号码:0767561235'
```

### 2.4 判断开头语结尾

| 字符 | 功能           |
| ---- | -------------- |
| ^    | 匹配字符串开头 |
| $    | 匹配字符串结尾 |

 

### 2.5 分组匹配

| 字符         | 功能                             |
| ------------ | -------------------------------- |
| \|           | 匹配左右任意一个表达式           |
| (ab)         | 将括号中字符作为一个分组         |
| `\num`       | 引用分组num匹配到的字符串        |
| `(?P<name>)` | 分组起别名                       |
| (?P=name)    | 引用别名为name分组匹配到的字符串 |

 3.分子匹配[¶](http://localhost:8888/notebooks/Desktop/GitHub/Python/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F/regular_expression.ipynb#3.%E5%88%86%E5%AD%90%E5%8C%B9%E9%85%8D)

In [48]:

```
# 邮箱匹配
import re

ret = re.match("\w{4,20}@163\.com", "test@163.com")
print(ret.group())  # test@163.com

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@126.com")
print(ret.group())  # test@126.com

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@qq.com")
print(ret.group())  # test@qq.com

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@gmail.com")
if ret:
    print(ret.group())
else:
    print("不是163、126、qq邮箱")  # 不是163、126、qq邮箱
```

Out[48]:

```
test@163.com
test@126.com
test@qq.com
不是163、126、qq邮箱
```

- ()与group使用
- group(num)num取到的值为()中的值。

In [52]:

```
result = re.match("([^-]*)-(\d+)","076-4561541")
```

```
result.group()
```

Out[53]:

```
'076-4561541'
```

In [54]:

```
result.group(1)
```

Out[54]:

```
'076'
```

In [55]:

```
result.group(2)
```

Out[55]:

```
'4561541'
```

- '\number'使用

In [57]:

```
#需求：匹配出<html><h1>www.itcast.cn</h1></html>
labels = ["<html><h1>www.itcast.cn</h1></html>", "<html><h1>www.itcast.cn</h2></html>"]
for label in labels:
    # 这里的\2 和\1表示（）2和（）1 的内容
    ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", label)
    if ret:
        print("%s 是符合要求的标签" % ret.group())
    else:
        print("%s 不符合要求" % label)
```

Out[57]:

```
<html><h1>www.itcast.cn</h1></html> 是符合要求的标签
<html><h1>www.itcast.cn</h2></html> 不符合要求
```

### 2.6 其他

#### Pattern

Pattern对象是一个编译好的正则表达式，通过Pattern提供的一系列方法可以对文本进行匹配查找。

Pattern不能直接实例化，必须使用re.compile()进行构造。

Pattern提供了几个可读属性用于获取表达式的相关信息：

- pattern: 编译时用的表达式字符串。
- flags: 编译时用的匹配模式。数字形式。
- groups: 表达式中分组的数量。
- groupindex: 以表达式中有别名的组的别名为键、以该组对应的编号为值的字典，没有别名的组不包含在内。

#### 使用Pattern

**match(string[, pos[, endpos]]) | re.match(pattern, string[, flags]):** 

这个方法将从string的pos下标处起尝试匹配pattern:

- 如果pattern结束时仍可匹配，则返回一个Match对象
- 如果匹配过程中pattern无法匹配，或者匹配未结束就已到达endpos，则返回None。
- pos和endpos的默认值分别为0和len(string)。 
  **注意：这个方法并不是完全匹配。当pattern结束时若string还有剩余字符，仍然视为成功。想要完全匹配，可以在表达式末尾加上边界匹配符'$'。**

**search(string[, pos[, endpos]]) | re.search(pattern, string[, flags]):** 

这个方法从string的pos下标处起尝试匹配pattern

- 如果pattern结束时仍可匹配，则返回一个Match对象
- 若无法匹配，则将pos加1后重新尝试匹配，直到pos=endpos时仍无法匹配则返回None。
- pos和endpos的默认值分别为0和len(string))

**split(string[, maxsplit]) | re.split(pattern, string[, maxsplit]):**

- 按照能够匹配的子串将string分割后返回列表。
- maxsplit用于指定最大分割次数，不指定将全部分割。

**findall(string[, pos[, endpos]]) | re.findall(pattern, string[, flags]):**

- 搜索string，以列表形式返回全部能匹配的子串。

**finditer(string[, pos[, endpos]]) | re.finditer(pattern, string[, flags]):**

- 搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。

**sub(repl, string[, count]) | re.sub(pattern, repl, string[, count]):** 

使用repl替换string中每一个匹配的子串后返回替换后的字符串。

- 当repl是一个字符串时，可以使用\id或\g、\g引用分组，但不能使用编号0。
- 当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。 count用于指定最多替换次数，不指定时全部替换。