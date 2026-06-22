import calendar as _cal
from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import MESES_ABBR, Event

MESES = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
    7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre",
}


@login_required
def calendar_view(request):
    today = date.today()
    try:
        year = int(request.GET.get("y", today.year))
        month = int(request.GET.get("m", today.month))
    except ValueError:
        year, month = today.year, today.month

    events = Event.objects.filter(date__year=year, date__month=month)
    event_colors = {e.date.day: e.color for e in events}

    cal = _cal.Calendar(firstweekday=6)  # Domingo primero (D L M X J V S)
    cells = []
    for d in cal.itermonthdates(year, month):
        in_month = d.month == month
        cells.append(
            {
                "num": d.day,
                "in_month": in_month,
                "today": d == today,
                "color": event_colors.get(d.day) if in_month else None,
            }
        )

    prev_month = (month - 1) or 12
    prev_year = year - 1 if month == 1 else year
    next_month = 1 if month == 12 else month + 1
    next_year = year + 1 if month == 12 else year

    context = {
        "active": "calendar",
        "cells": cells,
        "month_name": MESES[month],
        "year": year,
        "prev": {"m": prev_month, "y": prev_year},
        "next": {"m": next_month, "y": next_year},
        "upcoming": Event.objects.filter(date__gte=today)[:6],
    }
    return render(request, "calendario/list.html", context)
