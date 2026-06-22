from datetime import date

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from apps.calendario.models import Event
from apps.descuentos.models import Redemption
from apps.feed.models import Post

from .models import Restaurant

User = get_user_model()


def admin_required(view):
    def check(u):
        return u.is_authenticated and (u.is_admin_role or u.is_superuser)

    return user_passes_test(check, login_url="dashboard")(view)


@login_required
def dashboard(request):
    today = date.today()
    socios = User.objects.filter(role=User.Role.SOCIO, is_active=True).count()
    upcoming = Event.objects.filter(date__gte=today)[:3]
    next_assembly = (
        Event.objects.filter(date__gte=today, tag=Event.Tag.OBLIGATORIA).first()
        or Event.objects.filter(date__gte=today).first()
    )
    coupon = getattr(request.user, "coupon", None)
    context = {
        "active": "dashboard",
        "socios": socios,
        "docs_count": request.user.documents.count(),
        "coupon": coupon,
        "next_assembly": next_assembly,
        "upcoming": upcoming,
        "recent_posts": Post.objects.filter(is_published=True)[:5],
    }
    return render(request, "core/dashboard.html", context)


@login_required
def about(request):
    return render(
        request,
        "core/about.html",
        {"active": "about", "restaurants": Restaurant.objects.filter(active=True)},
    )


@login_required
def meets(request):
    today = date.today()
    events = Event.objects.filter(date__gte=today).exclude(platform="")[:6]
    return render(
        request, "core/meets.html", {"active": "meets", "events": events}
    )


@admin_required
def admin_panel(request):
    members = (
        User.objects.filter(role=User.Role.SOCIO)
        .select_related("coupon")
        .order_by("first_name", "last_name")
    )
    context = {
        "active": "admin",
        "members": members[:20],
        "total_socios": members.count(),
        "total_acciones": sum(m.acciones for m in members),
        "redeemed_today": Redemption.objects.filter(
            date=date.today(), status=Redemption.Status.CANJEADO
        ).count(),
    }
    return render(request, "core/admin_panel.html", context)
