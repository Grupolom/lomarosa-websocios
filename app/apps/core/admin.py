from django.contrib import admin

from .models import Announcement, Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["name", "zone", "rating", "order", "active"]
    list_editable = ["order", "active"]
    search_fields = ["name", "zone"]


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ["text", "active", "created_at"]
    list_editable = ["active"]
