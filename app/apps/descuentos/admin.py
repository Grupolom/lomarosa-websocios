from django.contrib import admin

from .models import Coupon, Redemption


class RedemptionInline(admin.TabularInline):
    model = Redemption
    extra = 0


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ["code", "owner", "percent", "redeemed_count", "max_redemptions", "active"]
    list_filter = ["active", "percent"]
    search_fields = ["code", "owner__email", "owner__first_name", "owner__last_name"]
    autocomplete_fields = ["owner"]
    inlines = [RedemptionInline]


@admin.register(Redemption)
class RedemptionAdmin(admin.ModelAdmin):
    list_display = ["coupon", "establishment", "date", "status"]
    list_filter = ["status", "date"]
    search_fields = ["coupon__code", "establishment"]
