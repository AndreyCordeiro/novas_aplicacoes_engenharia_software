from .models import Marca, Produto, Cliente, Pedido
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# CREATE


class MarcaCreate(LoginRequiredMixin, CreateView):
    model = Marca
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-marca")


class ProdutoCreate(LoginRequiredMixin, CreateView):
    model = Produto
    fields = ["nome", "preco", "codigo", "marca"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-produto")


class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ["nome", "cpf", "telefone"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cliente")


# UPDATE


class MarcaUpdate(LoginRequiredMixin, UpdateView):
    model = Marca
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-marca")


class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    model = Produto
    fields = ["nome", "preco", "codigo", "marca"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-produto")


class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ["nome", "cpf", "telefone"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cliente")


# LIST


class MarcaList(ListView):
    model = Marca
    template_name = "cadastros/list/marca.html"


class ProdutoList(ListView):
    model = Produto
    template_name = "cadastros/list/.html"


class ClienteList(ListView):
    model = Cliente
    template_name = "cadastros/list/.html"


# DELETE


class MarcaDelete(DeleteView):
    model = Marca
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-marca")


class ProdutoDelete(DeleteView):
    model = Produto
    template_name = "cadastros/list/delete.html"
    success_url = reverse_lazy("listar-produto")


class ClienteDelete(DeleteView):
    model = Cliente
    template_name = "cadastros/list/delete.html"
    success_url = reverse_lazy("listar-cliente")
