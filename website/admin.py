from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Thought)
class ToughtAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')

@admin.register(YoutubeLink)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')