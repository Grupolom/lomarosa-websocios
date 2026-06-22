from django.urls import path

from . import views

urlpatterns = [
    path("", views.feed_list, name="feed"),
    path("publicar/", views.post_create, name="post_create"),
    path("importar/", views.post_import, name="post_import"),
    path("importar/plantilla/", views.post_import_template, name="post_import_template"),
    path("<int:pk>/editar/", views.post_edit, name="post_edit"),
    path("<int:pk>/eliminar/", views.post_delete, name="post_delete"),
    path("<int:pk>/reaccion/", views.post_react, name="post_react"),
]
