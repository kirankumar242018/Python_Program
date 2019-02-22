from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = 'chat'
urlpatterns = [
    # /chat/
    path('', views.base, name='base'),

    path('login_and_register/', views.register_and_signup, name='login_and_register'),
    url(r'^home/', views.index, name='index'),
    url(r'^user_login/', views.loginchatview, name='loginchatview'),
    re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),


    # path('adduser/', views.addUser, name='addUser'),
    # url(r'^$', views.index, name='index'),
    # re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
