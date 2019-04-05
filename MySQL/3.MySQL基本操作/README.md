# MySQL操作

MySQL操作主要包括如下几个部分：

- 数据库操作
- 数据表操作
- 数据增删改查

## 1 数据库操作

- 链接数据库：

```
mysql -uroot -p
mysql -uroot -p密码
```

- 退出数据库

```
exit/quit/ctrl+d
```

- 查看所有数据库

```
show databases;
```

- 创建数据库

```
-- create database 数据库名 charset=utf8;
create database mysql_demo_100;
create database mysql_demo_200 charset=utf8;   -- 制定编码格式
```

- 查看创建数据库的语句

```
-- show crate database ....
show create database mysql_demo_100;
```

- 查看当前使用的数据库

```
select database();
```

- 使用数据库

```
-- use 数据库的名字
use mysql_demo_100;
```

- 删除数据库

```
-- drop database 数据库名;
drop database mysql_demo_100;
```
- 创建用户和授权

```
创建用户：
    create user 'hiram'@'192.168.1.1' identified by '123123';
    create user 'hiram'@'192.168.1.%' identified by '123123';
    create user 'hiram'@'%' identified by '123123';
授权：
	权限  人
        grant select,insert,update  on db1.t1 to 'hiram'@'%';
        grant all privileges  on db1.t1 to 'hiram'@'%';

        revoke all privileges on db1.t1 from 'hiram'@'%';
```

## 2 数据表操作

- 查看当前所有表

```
show tables;
```

- 创建表

```
-- auto_increment表示自动增长
-- not null 表示不能为空
-- primary key 表示主键
-- default 默认值
-- create table 数据表名字 (字段 类型 约束[, 字段 类型 约束]);
create table table_test_01(id int, name varchar(30));
create table table_test_02(id int primary key not null auto_increment, name varchar(30));
create table table_test_03(
id int primary key not null auto_increment,
name varchar(30)
);
```
案例：

    -- 创建students表(id、name、age、high、gender、cls_id)
    create table students(
        id int unsigned not null auto_increment primary key,
        name varchar(30),
        age tinyint unsigned default 0,
        high decimal(5,2),
        gender enum("男", "女", 保密") default "保密",
        cls_id int unsigned
    );
    
    -- 插入数据
    insert into students values(0, "小明", 20, 190.5, "男", 0);
    -- 查看表
    select * from students;
- 查看表结构

```
-- desc 数据表的名字;
desc table_test_01;
```

- 查看表创建

```
-- show create table 表名字;
show create table students;
```

- 修改表
1. 添加字段
```
-- alter table 表名 add 列名 类型;
alter table students add birthday datetime;
```

2. 修改字段：不重命名版

```
-- alter table 表名 modify 列名 类型及约束;
alter table students modify birthday date;
```

- 修改表-修改字段：重命名版

```
-- alter table 表名 change 原名 新名 类型及约束;
alter table students change birthday birth date default "2000-01-01";
```

- 修改表
```
-- alter table 表名 drop 列名;
alter table students drop high;
```
- 删除表
```
-- drop table 表名;
-- drop database 数据库;
-- drop table 数据表;
drop table students;
```
## 3 数据增删改查

### 3.1 增

- 全列插入
```
-- insert [into] 表名 values(...)
-- 主键字段 可以用 0  null   default 来占位
insert into students values(0, "18", 20, "男", 1, "2000-05-01");
```
向students表插入 一个学生信息：
```
insert into students values(0, "小明", 20, "女", 1, "2007-01-01");
insert into students values(null, "小明", 20, "女", 1, "2007-01-01");
insert into students values(default, "小明", 20, "女", 1, "2007-01-01");
```
对于这个执行的效果是一样的，因为id是自增的默认可以写以上的值。

枚举数据：

    -- 枚举中 的 下标从1 开始 1---“男” 2--->"女"....
    insert into students values(default, "小明", 20, 1, 1, "2007-09-12");
- 部分插入

```
-- insert into 表名(列1,...) values(值1,...)
insert into students (name, gender) values ("大明", 2);
```

- 多行插入
```
insert into students (name, gender) values ("李四", 2),("张三", 2);
insert into students values(default, "周杰伦", 20, "男", 1, "2000-01-01"), (default, "陈奕迅", 20, "男", 1, "2007-01-01");
```
### 3.2 改

```
-- update 表名 set 列1=值1,列2=值2... where 条件;
update students set gender=1; -- 全部都改
update students set gender=1 where name="小明"; -- 只要name是小明的 全部的修改
update students set gender=1 where id=3; -- 只要id为3的 进行修改
update students set age=22, gender=1 where id=3; -- 只要id为3的 进行修改
```

### 3.3 查

- 查询所有列

```
-- select * from 表名;
select * from students;
```

- 条件查询
```
select * from students where name="小明"; -- 查询 name为小明的所有信息
select * from students where id>3; -- 查询 id大于三的数据
```
- 指定列查询

```
-- select 列1,列2,... from 表名;
select name,gender from students;
```

- 使用as为列或者表制定别名进行查询
```
-- select 字段[as 别名] , 字段[as 别名] from 数据表 where ....;
select name as 姓名,gender as 性别 from students;
```
- 字段的顺序

```
select id as 序号, gender as 性别, name as 姓名 from students;
```

### 3.4 删

- 物理删除

```
-- delete from 表名 where 条件
delete from students; -- 整个数据表中的所有数据全部删除
delete from students where name="小明";
```

- 逻辑删除：不是真的对表中的数据进行删除

```
-- 用一个字段来表示 这条信息是否已经不能再使用了
-- 给students表添加一个is_delete字段 bit 类型
alter table students add is_delete bit default 0;
update students set is_delete=1 where id=6;
```

