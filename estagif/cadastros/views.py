from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from .models import Marca, Produto, Cliente, Pedido, Carrinho, ProdutoPedido
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from dal import autocomplete
from .forms import PedidoForms

# CREATE


class MarcaCreate(LoginRequiredMixin, CreateView):
    model = Marca
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-marca")
    extra_context = {"titulo": "Cadastro de Marca"}


class ProdutoCreate(LoginRequiredMixin, CreateView):
    model = Produto
    fields = ["nome", "preco", "codigo", "marca"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-produto")
    extra_context = {"titulo": "Cadastro de Produto"}


class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ["nome", "cpf", "telefone"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-cliente")
    extra_context = {"titulo": "Cadastro de Cliente"}


class PedidoCreate(LoginRequiredMixin, CreateView):
    form_class = PedidoForms
    template_name = "cadastros/form_pedido.html"
    success_url = reverse_lazy("listar-pedido")
    extra_context = {"titulo": "Cadastro de Pedido"}

    def form_valid(self, form):
        form.instance.valor_total = 0.0

        # cria a venda no banco e o object
        url = super().form_valid(form)

        # faz um select em todos os produtos do carirnho
        produtos_pedido = Carrinho.objects.all()
        valor_total = 0.0

        if (produtos_pedido.count() == 0):
            form.add_error("", "Seu carrinho de compras está vazio!")
            return super().form_invalid(form)

        for i in produtos_pedido:
            valor_total += (float(i.produto.preco) * i.quantidade)

            ProdutoPedido.objects.create(
                produto=i.produto,
                pedido=self.object,
                preco=i.produto.preco * i.quantidade,
                quantidade=i.quantidade
            )

            i.delete()

        self.object.valor_total = valor_total
        self.object.save()

        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["carrinho"] = Carrinho.objects.all()

        return context


class CarrinhoCreate(LoginRequiredMixin, CreateView):
    model = Carrinho
    fields = ["produto", "quantidade"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-carrinho")
    extra_context = {"titulo": "Adicionar item ao Carrinho"}

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


class CarrinhoUpdate(LoginRequiredMixin, UpdateView):
    model = Carrinho
    fields = ["produto", "quantidade"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-carrinho")

# LIST


class MarcaList(LoginRequiredMixin, ListView):
    model = Marca
    template_name = "cadastros/list/marca.html"
    paginate_by = 50


class ProdutoList(LoginRequiredMixin, ListView):
    model = Produto
    template_name = "cadastros/list/produto.html"
    paginate_by = 50


class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "cadastros/list/cliente.html"
    paginate_by = 50


class PedidoList(LoginRequiredMixin, ListView):
    model = Pedido
    template_name = "cadastros/list/pedido.html"
    paginate_by = 50

    # Melhora no desempenho da consulta, isso é um INNER JOIN no atributo CLIENTE
    def get_queryset(self):
        return Pedido.objects.all().select_related("cliente")


class CarrinhoList(LoginRequiredMixin, ListView):
    model = Carrinho
    template_name = "cadastros/list/carrinho.html"
    paginate_by = 50


class ProdutoPedidoList(LoginRequiredMixin, ListView):
    model: ProdutoPedido
    template_name = "cadastros/list/produto_pedido.html"

    def get_queryset(self):
        return ProdutoPedido.objects.filter(pedido__pk=self.kwargs["pk_pedido"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["pedido"] = Pedido.objects.get(pk=self.kwargs["pk_pedido"])

        return context


# DELETE


class MarcaDelete(LoginRequiredMixin, DeleteView):
    model = Marca
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-marca")


class ProdutoDelete(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = "cadastros/list/delete.html"
    success_url = reverse_lazy("listar-produto")


class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = "cadastros/list/delete.html"
    success_url = reverse_lazy("listar-cliente")


class PedidoDelete(LoginRequiredMixin, DeleteView):
    model = Pedido
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-pedido")


class CarrinhoDelete(LoginRequiredMixin, DeleteView):
    model = Carrinho
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-carrinho")


################################### AUTOCOMPLETE ###################################


class ClienteAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    def get_queryset(self):
        object_list = Cliente.objects.all()

        if self.q:
            object_list = object_list.filter(
                nome__icontains=self.q
            )

        return object_list
