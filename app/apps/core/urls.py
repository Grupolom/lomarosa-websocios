from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("aliados/", views.about, name="about"),
    path("reuniones/", views.meets, name="meets"),
    path("panel/", views.admin_panel, name="admin_panel"),
]
