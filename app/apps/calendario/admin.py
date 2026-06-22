from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "date", "time", "tag", "platform", "reminder"]
    list_filter = ["tag", "platform", "date"]
    search_fields = ["title", "description", "location"]
    date_hierarchy = "date"
