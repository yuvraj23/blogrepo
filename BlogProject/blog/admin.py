from django.contrib import admin
from blog.models import Post,Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status','tags']
    list_filter=('status','author','created','publish')
    prepopulated_fields={'slug':('title',)}
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'




class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','created','update','active')
    list_filter=('active','created','update')
    search_fields=('name','email','body')



admin.site.register(Comment,CommentAdmin)

admin.site.register(Post,PostAdmin)
