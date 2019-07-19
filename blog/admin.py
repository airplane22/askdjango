from django.contrib import admin

# Register your models here.
from .models import Post

#post를 커스텀하기

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =  ['id', 'title', 'created_at', 'updated_at']
    pass

#admin.site.register(Post, PostAdmin)

#register 두번 할 수 없음! 이미 register된 것을 unregister 하고 register 해야 함
#언제한다고??