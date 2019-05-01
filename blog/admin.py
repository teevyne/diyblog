from django.contrib import admin

# Register your models here.

from blog.models import Blog, Blogger, Language, Theme
admin.site.register(Blog)
admin.site.register(Blogger)
admin.site.register(Language)
admin.site.register(Theme)


