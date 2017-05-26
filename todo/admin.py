from django.contrib import admin

# Register your models here.

from .models import Todo, Label

# admin.site.register(Todo)
admin.site.register(Label)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'label', 'created_at')