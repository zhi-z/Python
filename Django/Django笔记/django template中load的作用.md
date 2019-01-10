# django template中load的作用

某些应用提供自定义标签和过滤器库. 要在一个模板中访问它们, 使用 {% load %} 标签:

{% load comments %} {% comment_form for blogs.entries entry.id with is_public yes %}

{% load %} 

标签可接受空隔分隔的多个库的名字作为参数.{% load comments i18n %}

当你载入一个自定义标签或过滤器库, 只有当前模板可以使用这些标签/过滤器 — 继承链中不论是父模板还是子模板都不能使用使用这些标签和过滤器.