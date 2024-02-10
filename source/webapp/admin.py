from django.contrib import admin
from .models import Category, Announcement, Comment


@admin.register(Announcement)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'img', 'heading', 'description', 'author', 'category', 'price', 'status', 'date_creation', 'date_publications', 'date_update']
    list_display_links = ['id', 'heading', 'description', 'author']
    list_filter = ['heading', 'author']
    search_fields = ['id', 'heading', 'author']
    fields = ['img', 'heading', 'description', 'author', 'category', 'price', 'status', 'date_creation', 'date_publications', 'date_update']
    readonly_fields = ['date_creation', 'date_publications', 'date_update']

@admin.register(Category)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']
    fields = ['name']

@admin.register(Comment)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'author', 'announcement_com', 'date_creation_com']
    list_display_links = ['id', 'text', 'author', 'announcement_com', 'date_creation_com']
    search_fields = ['id', 'text', 'author']
    fields = ['text', 'author', 'announcement_com', 'date_creation_com']
    readonly_fields = ['date_creation_com']
