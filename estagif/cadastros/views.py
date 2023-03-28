from .models import Marca, Produto, Cliente, Pedido
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# UPDATE
class MarcaCreate(CreateView):
    model = Marca
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class ProdutoCreate(CreateView):
    model = Produto
    fields = ["nome", "preco", "codigo", "marca"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


# UPDATE
class MarcaUpdate(UpdateView):
    model = Marca
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ["nome", "preco", "codigo", "marca"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")
