from django.urls import path
from . import views

urlpatterns = [
    path('ver_produtos/', views.ver_produtos, name="ver_produto"),
    path('inserir_produto/', views.inserir_produto, name="inserir_produto")
]