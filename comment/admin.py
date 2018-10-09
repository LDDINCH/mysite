from django.contrib import admin
from .models import Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('object_id','content_type','comment_text', 'comment_time','user', 'root')

# Register your models here.
