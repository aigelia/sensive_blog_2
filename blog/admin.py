from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at', 'author']
    raw_id_fields = ['author', 'likes', 'tags']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'published_at', 'text', 'post']
    raw_id_fields = ['author', 'post']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
