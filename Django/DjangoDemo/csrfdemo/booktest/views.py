from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def login_required(view_func):
    '''登录判断装饰器'''
    def wrapper(request, *view_args, **view_kwargs):
        # 判断用户是否登录
        if request.session.has_key('islogin'):
            # 用户已登录,调用对应的视图
            return view_func(request, *view_args, **view_kwargs)
        else:
            # 用户未登录,跳转到登录页
            return redirect('/login')
    return wrapper

    

def login(request):
    '''显示登录页面'''
    # 判断用户是否登录
    if request.session.has_key('islogin'):
        # 用户已登录, 跳转到首页
        return redirect('/change_pwd')
    else:
        # 用户未登录
        # 获取cookie username
        if 'username' in request.COOKIES:
            # 获取记住的用户名
            username = request.COOKIES['username']
        else:
            username = ''

        return render(request, 'booktest/login.html', {'username':username})


def login_check(request):
    '''登录校验视图'''
    # 1.获取提交的用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    # 2.进行登录的校验
    # 实际开发:根据用户名和密码查找数据库
    # 模拟: smart 123
    if username == 'smart' and password == '123':
        # 用户名密码正确
        response = redirect('/change_pwd')

        # 判断是否需要记住用户名
        if remember == 'on':
            # 设置cookie username，过期时间1周
            response.set_cookie('username', username, max_age=5)


        # 记住用户登录状态
        # 只有session中有islogin,就认为用户已登录
        request.session['islogin'] = True
        request.session['username'] = username

        # 返回应答
        return response
    else:
        # 用户名或密码错误，跳转到登录页面
        return redirect('/login')


def index(request):

    return render(request, 'booktest/index.html')

@login_required
def change_pwd(request):

	return render(request,'booktest/change_pwd.html')


def change_pwd_action(request):
    '''模拟修改密码处理'''
    # # 进行用户是否登录的判断
    # if not request.session.has_key('islogin'):
    #     # 用户未登录，跳转到登录
    #     return redirect('/login')

    # 1.获取新密码
    pwd = request.POST.get('pwd')
    # 获取用户名
    username = request.session.get('username')
    # 2.实际开发的时候: 修改对应数据库中的内容...
    # 3.返回一个应答
    return HttpResponse('%s修改密码为:%s'%(username,pwd))