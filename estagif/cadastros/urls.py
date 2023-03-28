from django.urls import path
from .views import MarcaCreate, MarcaUpdate
from .views import ProdutoCreate, ProdutoUpdate

urlpatterns = [
    path("cadastrar/marca", MarcaCreate.as_view(), name="cadastrar-marca"),
    path("atualizar/marca/<int:pk>/", MarcaUpdate.as_view(), name="atualizar-marca"),

    path("cadastrar/produto", ProdutoCreate.as_view(), name="cadastrar-produto"),
    path("atualizar/produto/<int:pk>/", ProdutoUpdate.as_view(), name="atualizar-produto"),
]