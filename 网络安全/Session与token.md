# Session与token

## 1 session

session意为“会话”。我们都知道HTTP是无状态的协议，但有时我们需要保存状态来进行后面的操作，比如某个电商网站的购物车功能（在不登录的情况下，也就是不使用数据库），如果不使用session，那么每次添加物品到购物篮后都不会保存，结果就是刷新一下购物篮就会变成空的。所以我们需要这个session来保存一定的状态。当用户打开某个网页的时候，就发生了一次会话，也就是产生了一个session，服务器会将session保存在服务器上，session中可能包括了用户信息，在用户离开网页之后，session就会被销毁。 

## 2 session与token区别

session和token作为用户登陆手段的区别

### 2.1 session的作用机理

session在每一次会话开始的时候产生，其中存放会话的信息，每一个session都有一个session_id。在账号密码登陆成功后，会在session保存相应的登陆状态，然后服务器会将这个session_id存放在cookie中发送给客户端，这样浏览器下次访问的时候，会带着cookie中的session_id进行访问，服务器再根据这个session_id来找到对应的session，再去session中查找相关信息判断用户是否能正常登陆。

### 2.2 token的作用机理

客户端传送用户名和密码到服务器请求登陆，服务器在验证通过后签发一个有时效性的token，将token返回给客户端。
客户端收到token之后将这个token存储起来，可以放在Cookie或者LocalStorage里。
以后客户端每次访问服务器都会带着这个token，服务器收到请求，会验证这个token，如果验证成功，就会向客户端放回请求的资源。

### 2.3 两者关系

看起来session的验证和token的验证很相似，都是从服务器返回一个数据，然后之后每次请求的时候都带着，发送给服务器验证。但其实是有很大不同的。

session的session_id只是一个唯一标识的字符串，本身不存放任何信息，需要通过这个session_id来找到session，session才存放了相应的信息，其中包括用户的登陆状态，就算没有请求登陆或者登陆没有成功，依然会有session和session_id。而token本身就是在登陆成功后才会签发并返回的，而且token是一些参数和随机数按照某种规则生成的字符串，其中一个参数就是用户的信息，也就是说token本身就存放了用户的相关信息。我们只需要在服务器验证这个token是否是合法的就可以了。

session的使用需要配合cookie，我们知道只有浏览器才会去解析请求响应头里面的cookie。但现在经常会出现前后端分离的写法，通常都是后端提供接口，前端我们的客户端不止是浏览器，还有APP等其他客户端。这个时候cookie是不起作用的。但是token就没有这些问题，token可以被APP存放在内存当中，本身不局限于浏览器。也就是说token有更广的适用性

作者：近光 
来源：CSDN 
原文：https://blog.csdn.net/ran_Max/article/details/80598514 
版权声明：本文为博主原创文章，转载请附上博文链接！