from django.contrib import admin

# Register your models here.

from .models import BoardMessage, Rubric

class BoardMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(BoardMessage, BoardMessageAdmin)
admin.site.register(Rubric)