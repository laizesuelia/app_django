from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("meuapp.urls")),
    path("catalogo/", include("catalogo.urls")),
    path("admin/", admin.site.urls),
]