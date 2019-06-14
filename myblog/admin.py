from django.contrib import admin
from .models import Post
from .models import Category


class PostAdmin(admin.ModelAdmin):
    pass

class InlineModelAdmin(admin.TabularInline):
    model = Category

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
