from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'date')
    search_fields = ('text',)
    date_hierarchy = 'date'
admin.site.register(Message, MessageAdmin)
