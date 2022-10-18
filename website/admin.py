from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(YoutubeLink)
class YoutubeLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')

@admin.register(Thought)
class ThoughtAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')