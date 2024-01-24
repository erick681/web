from django.urls import path
from .views import cadastro,listar
urlpatterns = [
    path('cadastro',cadastro,name ="cadastro"),
    path('listar',listar, name ="listar")
]
