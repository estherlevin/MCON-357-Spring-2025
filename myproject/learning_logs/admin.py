from django.contrib import admin
from .models import Topic, Entry

# Register your models here.
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_created')
    list_filter = ('date_created',)
    search_fields = ('name', 'description')

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('topic', 'title', 'content', 'date_created')
    list_filter = ('date_created',)
    search_fields = ('title', 'content')