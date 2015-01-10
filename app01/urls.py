from django.conf.urls import patterns,include, url

import views

urlpatterns = patterns('',
    (r'^$', views.index),      
    
    (r'^detail/(\d+)/$',views.bbs_detail),     
    (r'^sub_comment/$', views.sub_comment),
)