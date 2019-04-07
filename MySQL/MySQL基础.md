# MySQL 基础

## 1 MySQL安装

**Linux版本**

安装： 

```
yum install mysql-server　　
```

服务端启动

```
mysql.server start
```

客户端连接

```
连接：
    mysql -h host -u user -p
 
    常见错误：
        ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2), it means that the MySQL server daemon (Unix) or service (Windows) is not running.
退出：
    QUIT 或者 Control+D
```

## 2 数据库操作

### 2.1 显示数据库 

```
SHOW DATABASES;
```

> 默认数据库： 　
>
> ​	mysql - 用户权限相关数据　
>
> ​	test - 用于用户测试数据
>
> ​	information_schema - MySQL本身架构相关数据 

### 2.2 创建数据库

```
# utf-8
CREATE DATABASE 数据库名称 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
 
# gbk
CREATE DATABASE 数据库名称 DEFAULT CHARACTER SET gbk COLLATE gbk_chinese_ci;
```

### 2.3 使用数据库 

```
USE db_name;
```

显示当前使用的数据库中所有表：SHOW TABLES; 

### 2.4 用户管理 

```
创建用户
    create user '用户名'@'IP地址' identified by '密码';
删除用户
    drop user '用户名'@'IP地址';
修改用户
    rename user '用户名'@'IP地址'; to '新用户名'@'IP地址';;
修改密码
    set password for '用户名'@'IP地址' = Password('新密码')
  
PS：用户权限相关数据保存在mysql数据库的user表中，所以也可以直接对其进行操作（不建议）

```

### 2.5 授权管理 

```
show grants for '用户'@'IP地址'                  -- 查看权限
grant  权限 on 数据库.表 to   '用户'@'IP地址'      -- 授权
revoke 权限 on 数据库.表 from '用户'@'IP地址'      -- 取消权限
```

```
            all privileges  除grant外的所有权限
            select          仅查权限
            select,insert   查和插入权限
            ...
            usage                   无访问权限
            alter                   使用alter table
            alter routine           使用alter procedure和drop procedure
            create                  使用create table
            create routine          使用create procedure
            create temporary tables 使用create temporary tables
            create user             使用create user、drop user、rename user和revoke  all privileges
            create view             使用create view
            delete                  使用delete
            drop                    使用drop table
            execute                 使用call和存储过程
            file                    使用select into outfile 和 load data infile
            grant option            使用grant 和 revoke
            index                   使用index
            insert                  使用insert
            lock tables             使用lock table
            process                 使用show full processlist
            select                  使用select
            show databases          使用show databases
            show view               使用show view
            update                  使用update
            reload                  使用flush
            shutdown                使用mysqladmin shutdown(关闭MySQL)
            super                   􏱂􏰈使用change master、kill、logs、purge、master和set global。还允许mysqladmin􏵗􏵘􏲊􏲋调试登陆
            replication client      服务器位置的访问
            replication slave       由复制从属使用
```
对于数据库
```
对于目标数据库以及内部其他：
    数据库名.*           数据库中的所有
    数据库名.表          指定数据库中的某张表
    数据库名.存储过程     指定数据库中的存储过程
    *.*                所有数据库
```
对于用户
```
用户名@IP地址         用户只能在改IP下才能访问
用户名@192.168.1.%   用户只能在改IP段下才能访问(通配符%表示任意)
用户名@%             用户可以再任意IP下访问(默认IP地址为%)
```

实例

```
grant all privileges on db1.tb1 TO '用户名'@'IP'

grant select on db1.* TO '用户名'@'IP'

grant select,insert on *.* TO '用户名'@'IP'

revoke select on db1.tb1 from '用户名'@'IP'
```
特殊的： 

```
flush privileges，将数据读取到内存中，从而立即生效。 
```

忘记密码

```
# 启动免授权服务端
mysqld --skip-grant-tables

# 客户端
mysql -u root -p

# 修改用户名密码
update mysql.user set authentication_string=password('666') where user='root';
flush privileges;
```

## 3 数据表基本操作

### 3.1 创建表 

```
create table 表名(
    列名  类型  是否可以为空，
    列名  类型  是否可以为空
)ENGINE=InnoDB DEFAULT CHARSET=utf8
```

是否为空：

> 
>   是否可空，null表示空，非字符串
>         not null    - 不可空
>         null        - 可空
> 

默认值

```
默认值，创建列时可以指定默认值，当插入数据时如果未主动设置，则自动添加默认值
create table tb1(
    nid int not null defalut 2,
    num int not null
)
```

自增：自增，如果为某列设置自增列，插入数据时无需设置此列，默认将自增（表中只能有一个自增列）

```
create table tb1(
    nid int not null auto_increment primary key,
    num int null
)
或
create table tb1(
    nid int not null auto_increment,
    num int null,
    index(nid)
)
注意：
1、对于自增列，必须是索引（含主键）。
2、对于自增可以设置步长和起始值
    show session variables like 'auto_inc%';
    set session auto_increment_increment=2;
    set session auto_increment_offset=10;

    shwo global  variables like 'auto_inc%';
    set global auto_increment_increment=2;
    set global auto_increment_offset=10;

```

主键：主键，一种特殊的唯一索引，不允许有空值，如果主键使用单个列，则它的值必须唯一，如果是多列，则其组合必须唯一。

```
create table tb1(
    nid int not null auto_increment primary key,
    num int null
)	
或
create table tb1(
    nid int not null,
    num int not null,
    primary key(nid,num)
)
```

外键：外键，一个特殊的索引，只能是指定内容

```
creat table color(
    nid int not null primary key,
    name char(16) not null
)

create table fruit(
    nid int not null primary key,
    smt char(32) null ,
    color_id int not null,
    constraint fk_cc foreign key (color_id) references color(nid)
)
```

### 3.2 删除表

```
drop table 表名
```

### 3.3 清空表

```
delete from 表名
truncate table 表名
```

### 3.4 修改表

```
添加列：alter table 表名 add 列名 类型
删除列：alter table 表名 drop column 列名
修改列：
        alter table 表名 modify column 列名 类型;  -- 类型
        alter table 表名 change 原列名 新列名 类型; -- 列名，类型
  
添加主键：
        alter table 表名 add primary key(列名);
删除主键：
        alter table 表名 drop primary key;
        alter table 表名  modify  列名 int, drop primary key;
  
添加外键：alter table 从表 add constraint 外键名称（形如：FK_从表_主表） foreign key 从表(外键字段) references 主表(主键字段);
删除外键：alter table 表名 drop foreign key 外键名称
  
修改默认值：ALTER TABLE testalter_tbl ALTER i SET DEFAULT 1000;
删除默认值：ALTER TABLE testalter_tbl ALTER i DROP DEFAULT;
```

## 4 数据类型

MySQL的数据类型大致分为：数值、时间和字符串 

```
        bit[(M)]
            二进制位（101001），m表示二进制位的长度（1-64），默认m＝1

        tinyint[(m)] [unsigned] [zerofill]

            小整数，数据类型用于保存一些范围的整数数值范围：
            有符号：
                -128 ～ 127.
            无符号：
                0 ～ 255

            特别的： MySQL中无布尔值，使用tinyint(1)构造。

        int[(m)][unsigned][zerofill]

            整数，数据类型用于保存一些范围的整数数值范围：
                有符号：
                    -2147483648 ～ 2147483647
                无符号：
                    0 ～ 4294967295

            特别的：整数类型中的m仅用于显示，对存储范围无限制。例如： int(5),当插入数据2时，select 时数据显示为： 00002

        bigint[(m)][unsigned][zerofill]
            大整数，数据类型用于保存一些范围的整数数值范围：
                有符号：
                    -9223372036854775808 ～ 9223372036854775807
                无符号：
                    0  ～  18446744073709551615

        decimal[(m[,d])] [unsigned] [zerofill]
            准确的小数值，m是数字总个数（负号不算），d是小数点后个数。 m最大值为65，d最大值为30。

            特别的：对于精确数值计算时需要用此类型
                   decaimal能够存储精确值的原因在于其内部按照字符串存储。

        FLOAT[(M,D)] [UNSIGNED] [ZEROFILL]
            单精度浮点数（非准确小数值），m是数字总个数，d是小数点后个数。
                无符号：
                    -3.402823466E+38 to -1.175494351E-38,
                    0
                    1.175494351E-38 to 3.402823466E+38
                有符号：
                    0
                    1.175494351E-38 to 3.402823466E+38

            **** 数值越大，越不准确 ****

        DOUBLE[(M,D)] [UNSIGNED] [ZEROFILL]
            双精度浮点数（非准确小数值），m是数字总个数，d是小数点后个数。

                无符号：
                    -1.7976931348623157E+308 to -2.2250738585072014E-308
                    0
                    2.2250738585072014E-308 to 1.7976931348623157E+308
                有符号：
                    0
                    2.2250738585072014E-308 to 1.7976931348623157E+308
            **** 数值越大，越不准确 ****


        char (m)
            char数据类型用于表示固定长度的字符串，可以包含最多达255个字符。其中m代表字符串的长度。
            PS: 即使数据小于m长度，也会占用m长度
        varchar(m)
            varchars数据类型用于变长的字符串，可以包含最多达255个字符。其中m代表该数据类型所允许保存的字符串的最大长度，只要长度小于该最大值的字符串都可以被保存在该数据类型中。

            注：虽然varchar使用起来较为灵活，但是从整个系统的性能角度来说，char数据类型的处理速度更快，有时甚至可以超出varchar处理速度的50%。因此，用户在设计数据库时应当综合考虑各方面的因素，以求达到最佳的平衡

        text
            text数据类型用于保存变长的大字符串，可以组多到65535 (2**16 − 1)个字符。

        mediumtext
            A TEXT column with a maximum length of 16,777,215 (2**24 − 1) characters.

        longtext
            A TEXT column with a maximum length of 4,294,967,295 or 4GB (2**32 − 1) characters.


        enum
            枚举类型，
            An ENUM column can have a maximum of 65,535 distinct elements. (The practical limit is less than 3000.)
            示例：
                CREATE TABLE shirts (
                    name VARCHAR(40),
                    size ENUM('x-small', 'small', 'medium', 'large', 'x-large')
                );
                INSERT INTO shirts (name, size) VALUES ('dress shirt','large'), ('t-shirt','medium'),('polo shirt','small');

        set
            集合类型
            A SET column can have a maximum of 64 distinct members.
            示例：
                CREATE TABLE myset (col SET('a', 'b', 'c', 'd'));
                INSERT INTO myset (col) VALUES ('a,d'), ('d,a'), ('a,d,a'), ('a,d,d'), ('d,a,d');

        DATE
            YYYY-MM-DD（1000-01-01/9999-12-31）

        TIME
            HH:MM:SS（'-838:59:59'/'838:59:59'）

        YEAR
            YYYY（1901/2155）

        DATETIME

            YYYY-MM-DD HH:MM:SS（1000-01-01 00:00:00/9999-12-31 23:59:59    Y）

        TIMESTAMP

            YYYYMMDD HHMMSS（1970-01-01 00:00:00/2037 年某时）
```

*二进制数据：TinyBlob、Blob、MediumBlob、LongBlob* 

更多参考：

- http://www.runoob.com/mysql/mysql-data-types.html
- http://dev.mysql.com/doc/refman/5.7/en/data-type-overview.html

### 5 表内容操作

### 5.1 增

```
insert into 表 (列名,列名...) values (值,值,值...)
insert into 表 (列名,列名...) values (值,值,值...),(值,值,值...)
insert into 表 (列名,列名...) select (列名,列名...) from 表
```

### 5.2 删

```
delete from 表
delete from 表 where id＝1 and name＝'alex'
```

### 5.3 改

```
update 表 set name ＝ 'alex' where id>1
```

### 5.4 查

```
select * from 表
select * from 表 where id > 1
select nid,name,gender as gg from 表 where id > 1
```

### 5.4 其他

```
a、条件
    select * from 表 where id > 1 and name != 'alex' and num = 12;
 
    select * from 表 where id between 5 and 16;
 
    select * from 表 where id in (11,22,33)
    select * from 表 where id not in (11,22,33)
    select * from 表 where id in (select nid from 表)
 
b、通配符
    select * from 表 where name like 'ale%'  - ale开头的所有（多个字符串）
    select * from 表 where name like 'ale_'  - ale开头的所有（一个字符）
 
c、限制
    select * from 表 limit 5;            - 前5行
    select * from 表 limit 4,5;          - 从第4行开始的5行
    select * from 表 limit 5 offset 4    - 从第4行开始的5行
 
d、排序
    select * from 表 order by 列 asc              - 根据 “列” 从小到大排列
    select * from 表 order by 列 desc             - 根据 “列” 从大到小排列
    select * from 表 order by 列1 desc,列2 asc    - 根据 “列1” 从大到小排列，如果相同则按列2从小到大排序
 
e、分组
    select num from 表 group by num
    select num,nid from 表 group by num,nid
    select num,nid from 表  where nid > 10 group by num,nid order nid desc
    select num,nid,count(*),sum(score),max(score),min(score) from 表 group by num,nid
 
    select num from 表 group by num having max(id) > 10
 
    特别的：group by 必须在where之后，order by之前
 
f、连表
    无对应关系则不显示
    select A.num, A.name, B.name
    from A,B
    Where A.nid = B.nid
 
    无对应关系则不显示
    select A.num, A.name, B.name
    from A inner join B
    on A.nid = B.nid
 
    A表所有显示，如果B中无对应关系，则值为null
    select A.num, A.name, B.name
    from A left join B
    on A.nid = B.nid
 
    B表所有显示，如果B中无对应关系，则值为null
    select A.num, A.name, B.name
    from A right join B
    on A.nid = B.nid
 
g、组合
    组合，自动处理重合
    select nickname
    from A
    union
    select name
    from B
 
    组合，不处理重合
    select nickname
    from A
    union all
    select name
    from B
```

