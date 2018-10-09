from django.contrib import admin
from .models import BlogType, Blog


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name',)
    search_fields = ('id', 'type_name')
    list_filter = ('id', 'type_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'blog_type', 'createtime','get_read_num', 'last_update_time', 'author')
    search_fields = ('id','title', 'blog_type', 'createtime','get_read_num', 'last_update_time', 'author')
    list_filter = ('id','title', 'blog_type', 'createtime', 'last_update_time', 'author')



# @admin.register(ReadNum)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('read_num','blog')



