from django.contrib import admin
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    # это свойство сработает для всех колонок: где пусто - там будет эта строка
    empty_value_display = "-пусто-"


# при регистрации модели Post источником конфигурации для неё назначаем класс PostAdmin
admin.site.register(Post, PostAdmin)


# Register your models here.
class GroupAdmin(admin.ModelAdmin):
    list_display = ("slug", "title", "description")
    search_fields = ("description",)
    list_filter = ('title',)
    empty_value_display = "-пусто-"


# при регистрации модели Post источником конфигурации для неё назначаем класс PostAdmin
admin.site.register(Group, GroupAdmin)
