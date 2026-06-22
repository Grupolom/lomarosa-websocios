from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Redemption


@login_required
def my_coupon(request):
    coupon = getattr(request.user, "coupon", None)

    if request.method == "POST" and coupon:
        messages.success(
            request, f"Cupón {coupon.code} enviado a {request.user.email}"
        )
        return redirect("discounts")

    if request.user.is_admin_role or request.user.is_superuser:
        history = Redemption.objects.select_related("coupon", "coupon__owner").all()[:20]
    else:
        history = coupon.redemptions.all() if coupon else []

    return render(
        request,
        "descuentos/detail.html",
        {"active": "discounts", "coupon": coupon, "history": history},
    )
