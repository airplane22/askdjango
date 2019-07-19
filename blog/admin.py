from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from .models import Post

#post를 커스텀하기

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =  ['id', 'title', 'content_size', 'created_at', 'updated_at']

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))

    content_size.short_description = '글자수'
    #content_size.allow_tags = True

#admin.site.register(Post, PostAdmin)

#register 두번 할 수 없음! 이미 register된 것을 unregister 하고 register 해야 함
#언제한다고??