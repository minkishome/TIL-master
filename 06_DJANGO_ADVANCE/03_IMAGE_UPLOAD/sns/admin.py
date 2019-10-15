from django.contrib import admin
from .models import Posting

# Register your models here.
class PostingModleAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at',)
    list_display = ('id', 'content', 'create_at', 'update_at')
    list_display_links = ('id', 'content')



admin.site.register(Posting, PostingModleAdmin)