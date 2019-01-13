# rest framework序列化

## 1 序列化方式

### 1.1 方式1：

```
class PublishView(APIView):
    def get(self,request):

        # restframework
        # 取数据
        print("request.data", request.data)
        print("request.data type", type(request.data))
        print(request._request.GET)
        print(request.GET)
        # 序列化
        方式1：
        publish_list=list(Publish.objects.all().values("name","email"))
	    return HttpResponse(json.dumps(publish_list))
```

### 1.2 方式2：

```
class PublishView(APIView):
    def get(self,request):

        # restframework
        # 取数据
        print("request.data", request.data)
        print("request.data type", type(request.data))
        print(request._request.GET)
        print(request.GET)
        # 序列化----------------------------------------------
        # 方式2：
        from django.forms.models import model_to_dict
        publish_list=Publish.objects.all()
        temp=[]
        for obj in publish_list:
            temp.append(model_to_dict(obj))
		return HttpResponse(json.dumps(temp))
```

### 1.3 方式3：

```
class PublishView(APIView):
    def get(self,request):

        # restframework
        # 取数据
        print("request.data", request.data)
        print("request.data type", type(request.data))
        print(request._request.GET)
        print(request.GET)
        
        publish_list=list(Publish.objects.all().values("name","email"))
        # 序列化
        # 方式3：
        from django.core import serializers
        ret=serializers.serialize("json",publish_list)
	    rerurn HttpResponse(ret)
```

### 1.4 方式4：

先定义一个类：

```
class PublishModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=Publish
        fields="__all__"
```

然后调用这个类进行序列化：

```
class PublishView(APIView):
    def get(self,request):

        # restframework
        # 取数据
        # print("request.data", request.data)
        # print("request.data type", type(request.data))
        # print(request._request.GET)
        # print(request.GET)
        # 序列化
		
        # 序列组件
        publish_list = Publish.objects.all()
        ps = PublishModelSerializers(publish_list, many=True)
        return Response(ps.data)

```

## 2 序列化使用

序列化代码：

```
from rest_framework import serializers

from app01.models import *
# 为queryset,model对象做序列化
class PublishSerializers(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()

# 方法二：
class PublishModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=Publish
        fields="__all__"
	# 自定义设置显示，如下：
#     一对多
#     publish=serializers.CharField(source="publish.name")
#     #authors=serializers.CharField(source="authors.all")
#     多对多
#     authors = serializers.SerializerMethodField()
#     def get_authors(self,obj):
#         temp=[]
#         for obj in obj.authors.all():
#             temp.append(obj.name)
#         return temp)

#  注意：对于 一对多和多对多的情况默认显示的是键值，
#  如果想要进行修改，可以在该类中加入方法一中一对多和多对多这两种情况的定义


# 方法一：这个方法太复杂，可以不用
# class BookSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=32)
#     price = serializers.IntegerField()
#     pub_date = serializers.DateField()
#     一对多
#     publish=serializers.CharField(source="publish.name")
#     #authors=serializers.CharField(source="authors.all")
#     多对多
#     authors = serializers.SerializerMethodField()
#     def get_authors(self,obj):
#         temp=[]
#         for obj in obj.authors.all():
#             temp.append(obj.name)
#         return temp

'''
序列化BookSerializers(book_list,many=True)过程：
     temp=[]
     for obj in book_list:
         temp.append({
            "title":obj.title,
            "price":obj.price,
            "pub_date":obj.pub_date,
            "publish":str(obj.publish), # obj.publish.name
            #"authors":obj.authors.all,
            "authors": get_authors(obj)
         })

'''


class BookModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    #publish=serializers.CharField(source="publish.pk")
    publish=serializers.HyperlinkedIdentityField(
            view_name="detailpublish",
            lookup_field="publish_id",
            lookup_url_kwarg="pk"
    )


    # authors=serializers.CharField(source="authors.all")
    # authors = serializers.SerializerMethodField()
    # def get_authors(self,obj):
    #     temp=[]
    #     for obj in obj.authors.all():
    #         temp.append(obj.name)
    #     return temp

	### 重写create方法，因为用以上的自定义authors=serializers.CharField(source="authors.all")不支持，会报错
	### 如果重新定制publish ,则需要重写create方法
    # def create(self, validated_data):
    #     print("validated_data",validated_data)
    #     book=Book.objects.create(title=validated_data["title"],price=validated_data["price"],pub_date=validated_data["pub_date"],publish_id=validated_data["publish"]["pk"])
    #     book.authors.add(*validated_data["authors"])
    #
    #     return book
```

使用系列化返回数据，提供api：

```

class PublishDetailView(APIView):
    def get(self, request, pk):

        publish = Publish.objects.filter(pk=pk).first()
        ps = PublishModelSerializers(publish)
        return Response(ps.data)

    def put(self, request, pk):
        publish = Publish.objects.filter(pk=pk).first()
        ps = PublishModelSerializers(publish, data=request.data)
        if ps.is_valid():
            ps.save()
            return Response(ps.data)
        else:
            return Response(ps.errors)

    def delete(self, request, pk):
        Publish.objects.filter(pk=pk).delete()

        return Response()


class BookView(APIView):
    def get(self,request):
        book_list=Book.objects.all()
        bs=BookModelSerializers(book_list,many=True,context={'request': request})
        return Response(bs.data)
    def post(self,request):
        # post请求的数据
        bs=BookModelSerializers(data=request.data)
        if bs.is_valid():
            print(bs.validated_data)
            bs.save()# create方法
            return Response(bs.data)
        else:
            return Response(bs.errors)

class BookDetailView(APIView):

    def get(self,request,id):

        book=Book.objects.filter(pk=id).first()
        bs=BookModelSerializers(book,context={'request': request})
        return Response(bs.data)

    def put(self,request,id):
        book=Book.objects.filter(pk=id).first()
        bs=BookModelSerializers(book,data=request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)

    def delete(self,request,id):
        Book.objects.filter(pk=id).delete()

        return Response()
```

url配置：

```
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^publishes/$', views.PublishView.as_view(),name="publish"), #  View:view(request)=====APIView:dispatch()
    url(r'^publishes/(?P<pk>\d+)/$', views.PublishDetailView.as_view(),name="detailpublish"), #  View:view(request)=====APIView:dispatch()

    url(r'^books/$', views.BookView.as_view(),name="books"),
    url(r'^books/(\d+)/$', views.BookDetailView.as_view(),name="detailbook"),
    #url(r'^books/(\d+)/$', View:view),     # view(request)

    url(r'^authors/$', views.AuthorModelView.as_view({"get":"list","post":"create"}),name="author"),
    url(r'^authors/(?P<pk>\d+)/$', views.AuthorModelView.as_view({"get":"retrieve","put":"update","delete":"destroy"}),name="detailauthor"),

    url(r'^login/$', views.LoginView.as_view(),name="login"),

]
```

