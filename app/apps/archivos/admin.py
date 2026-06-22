from django.contrib import admin

from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ["name", "owner", "status", "size_label", "created_at"]
    list_filter = ["status", "created_at"]
    search_fields = ["name", "owner__email", "owner__first_name", "owner__last_name"]
    autocomplete_fields = ["owner", "uploaded_by"]

    def save_model(self, request, obj, form, change):
        if not obj.uploaded_by_id:
            obj.uploaded_by = request.user
        super().save_model(request, obj, form, change)
