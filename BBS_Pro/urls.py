from django.conf.urls import patterns, include, url
from django.contrib import admin
from app01 import views
import app01.urls

urlpatterns = patterns('',
#     (r'^accounts/login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
    (r'^login/$', views.Login ),
    (r'^logout/$', views.logout_view),
    (r'^register/$', views.Register),
    (r'^acc_login/$',views.acc_login),
    (r'^acc_register/$',views.acc_register),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(app01.urls)),
    
)
