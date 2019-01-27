from django.conf.urls import include, url
from django.contrib import admin
from vi import views as v

urlpatterns = [
    # Examples:
    # url(r'^$', 'views_exercise.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^teacher/', v.teacher),
    url(r'^v2_exp/', v.v2_exception)
]
