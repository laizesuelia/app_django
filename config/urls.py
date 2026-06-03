from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("meuapp.urls")),
    path("admin/", admin.site.urls),
]