# Django URL分发

## 1 简单的URL分发

```
# 视图函数
def test01(request):
	return HttpResponse("test01")
def test02(request):
	return HttpResponse("test02")
def test03(request):
	return HttpResponse("test03")
def test04(request):
	return HttpResponse("test04")
def test05(request):
	return HttpResponse("test04")
def test06(request):
	return HttpResponse("test04")
	
	
urlpatterns = [
    url(r'^index',([
        url(r^'test01/',([
            url(r^'test02/',test05),
            url(r^'test02/',test06),
        ],None,None)),
        url(r^'test02/',test02),
        url(r^'test03/',test03),
        url(r^'test04/',test04),
    ],None,None))
  
]

```



## 2 Django URL分发设计

```
def test01(request):
    return HttpResponse("test01")
def test02(request):
    return HttpResponse("test02")
def test03(request):
    return HttpResponse("test03")
def test04(request):
    return HttpResponse("test04")
def test05(request):
    return HttpResponse("test05")


def list_view(request):
    return HttpResponse("list_view")

def add_view(request):
    return HttpResponse("add_view")

def change_view(request,id):
    return HttpResponse("change_view")

def delete_view(request,id):
    return HttpResponse("delete_view")



def get_urls_2():

    temp=[]

    temp.append(url(r"^$",list_view))
    temp.append(url(r"^add/$",add_view))
    temp.append(url(r"^(\d+)/change/$",change_view))
    temp.append(url(r"^(\d+)/delete/$",delete_view))


    return temp


def get_urls():
    print(admin.site._registry)  # {Book:modelAdmin(Book),.......}


    temp=[]
    for model,admin_class_obj in admin.site._registry.items():
        app_name=model._meta.app_label
        model_name=model._meta.model_name

        temp.append(url(r'^{0}/{1}/'.format(app_name,model_name), (get_urls_2(),None,None)),)

    return temp


urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^Xadmin/', (get_urls(),None,None)),

]
```

