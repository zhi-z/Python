# 正则表达式

用于匹配字符串的，在这里使用Python实现。主要分为几大类：

- 匹配单个字符
- 匹配多个字符
- 匹配开头结尾
- 匹配分组

## 1 re 模块使用

- 基本流程
  - 导入re模块
  - 使用match方法进行匹配操作,result = re.match(正则表达式，要匹配的字符串)
  - 通group方法提取匹配的数据,result.group()
- 案例：

```python
import re
```

```python
# 满足正则表达式的就会有返回值
result = re.match(r"hello","hello raindi")
```

```python
result.group()
```

```
'hello'
```

