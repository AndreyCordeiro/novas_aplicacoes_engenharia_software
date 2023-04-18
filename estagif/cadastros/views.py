from .models import Marca, Produto, Cliente, Pedido
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# CREATE


class MarcaCreate(LoginRequiredMixin, CreateView):
    model = Marca
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class ProdutoCreate(LoginRequiredMixin, CreateView):
    model = Produto
    fields = ["nome", "preco", "codigo", "marca"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


# UPDATE


class MarcaUpdate(LoginRequiredMixin, UpdateView):
    model = Marca
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    model = Produto
    fields = ["nome", "preco", "codigo", "marca"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")
