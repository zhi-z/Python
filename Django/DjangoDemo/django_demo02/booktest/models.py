from django.db import models

# Create your models here.
class BookInfo(models.Model):
    '''图书模型类'''
    # 图书名称
    btitle = models.CharField(max_length=20)
    # 图书名字唯一
    # btitle = models.CharField(max_length=20, unique=True, db_index=True)
    # 价格,最大位数为10,小数为2
    # bprice = models.DecimalField(max_digits=10, decimal_places=2)
    # 出版日期
    bpub_date = models.DateField()
    # bpub_date = models.DateField(auto_now_add=True) # 创建时间
    # bpub_date = models.DateField(auto_now=True) # 更新时间
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除标记
    isDelete = models.BooleanField(default=False)


# 多类
class HeroInfo(models.Model):
    '''英雄人物模型类'''
    # 英雄名
    hname = models.CharField(max_length=20)
    # 性别
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=200)
    #　关系属性
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    # 删除标记
    isDelete = models.BooleanField(default=False)


