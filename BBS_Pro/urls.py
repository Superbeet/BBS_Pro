from django.conf.urls import patterns, include, url
from django.contrib import admin
from app01 import views
import app01.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^accounts/login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
    (r'^login/$', views.Login ),
    (r'^acc_login/$',views.acc_login),
    (r'^logout/$', views.logout_view),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(app01.urls)),
    
)
