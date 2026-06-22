def portal_context(request):
    """Datos compartidos por todas las plantillas del portal (sidebar, banner)."""
    ctx = {"announcement": None, "nav_news_count": 0}

    if not request.user.is_authenticated:
        return ctx

    from apps.core.models import Announcement
    from apps.feed.models import Post

    ctx["nav_news_count"] = Post.objects.filter(is_published=True).count()
    ctx["announcement"] = Announcement.objects.filter(active=True).first()
    return ctx
