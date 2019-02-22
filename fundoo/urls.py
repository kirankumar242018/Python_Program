from django.urls import path, include, re_path
from django.conf.urls import url

from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # rest api url
    # path('', views.UserListView.as_view()),

    # test this one
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),

    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    # path('index/', views.index, name='index'),


    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate,
        name='activate'),

    #  registration reset password,conformation...

    # url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),














    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='fundoo/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='fundoo/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='fundoo/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='fundoo/password_reset_complete.html'
         ),
         name='password_reset_complete'),


]