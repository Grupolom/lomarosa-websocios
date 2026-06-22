from django.contrib import admin

from .models import Post, Proposal


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "reactions", "is_published", "created_at"]
    list_filter = ["category", "is_published", "created_at"]
    search_fields = ["title", "excerpt", "body"]
    list_editable = ["is_published"]
    date_hierarchy = "created_at"


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ["author", "created_at"]
    search_fields = ["text"]
    readonly_fields = ["author", "text", "created_at"]
