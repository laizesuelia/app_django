from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sobre/", views.sobre, name="sobre"),
    path("contato/", views.contato, name="contato"),
    path("aluno/<int:id_aluno>", views.aluno, name="aluno"),
]