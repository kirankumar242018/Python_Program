from django.conf.urls import url

from django.contrib import admin
from django.urls import include, path,re_path
from chat import views

urlpatterns = [

    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    url(r'^home/', views.index, name='index'),

    # url('home/', views.index, name='index'),
    # path('chatmsg/', views.chatView, name='chatview'),

    url(r'^user_login/', views.loginchatview, name='loginchatview'),
    path('login_and_register/', views.register_and_signup, name='login_and_register'),
    path('adduser/', views.addUser, name='addUser'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),

]
