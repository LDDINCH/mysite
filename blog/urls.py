# _*_ encoding:utf-8 _*_
__author__ = "ludada"
__date__ = "2018/9/25 19:29"
from django.urls import path
from blog.views import blog_detail, blog_type_list, blog_list, blog_with_dates
app_name ='[blog]'
urlpatterns = [
    path('blog_list', blog_list, name='blog_list'),
    path('<int:blog_id>', blog_detail, name='blog_detail'),
    path('blog_type_list/<int:blog_type_id>',blog_type_list, name='blog_type_list' ),
    path('date/<int:year>/<int:month>', blog_with_dates, name='blog_dates'),
    ]