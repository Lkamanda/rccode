from django.conf.urls import include, url
from django.contrib import admin

from teacher import views as tv
from teacher import teacher_urls
urlpatterns = [
    # Examples:
    # url(r'^$', 'xl.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # 在路由中添加映射
    # 视图函数名称，只有名称，无括号和参数

    url(r'^nomalmap/', tv.do_nomalmap,name='normal'),
    # 带参数的例子
    url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])', tv.withparam),
    # 子路由例子
    url(r'^teacher/', include(teacher_urls)),
    # 带参数例子
    url(r'^book/(?:page-(?P<pagenumber>\d+)/)$', tv.do_book),

    # 额外参数
    url(r'^school/$', tv.do_param, {'name': 'xiaolin'}),
    url(r'^youname/$', tv.revParse, name="aaa"),

]
