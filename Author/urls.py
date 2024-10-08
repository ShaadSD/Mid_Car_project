from django.contrib import admin
from django.urls import path
from . import views


urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    path('login/',views.user_login,name='user_login'),
    path('pass_chang/',views.pass_change,name='pass_chang'),
    path('Edit_profile/',views.Edit_profile,name='Edit_profile'),
    path('logout/',views.user_logout,name='user_logout'),
    path('logout/',views.user_logout,name='user_logout'),
]
 