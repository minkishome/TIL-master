from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'title'#반드시 이 이름



admin.site.register(Article, ArticleModelAdmin)