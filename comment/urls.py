# _*_ encoding:utf-8 _*_
__author__ = "ludada"
__date__ = "2018/9/28 21:12"
from django.urls import path
from . import views

app_name ='[comment]'
urlpatterns = [
    path('update_comment', views.update_comment, name='update_comment')
]