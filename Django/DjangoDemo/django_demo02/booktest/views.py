from django.shortcuts import render,redirect
from booktest.models import *
from datetime import date

#查询所有图书并显示
def index(request):
    books = BookInfo.objects.all()
    return render(request,'booktest/index.html',{'books':books})

#创建新图书
def create(request):
    book=BookInfo()
    book.btitle = '流星蝴蝶剑'
    book.bpub_date = date(1995,12,30)
    book.save()
    #转向到首页
    return redirect('/index')

#逻辑删除指定编号的图书
def delete(request,id):
    book=BookInfo.objects.get(id=int(id))
    book.delete()
    #转向到首页
    return redirect('/index')


