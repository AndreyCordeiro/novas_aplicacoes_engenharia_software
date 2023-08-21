from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from cadastros.models import Cliente, Pedido, Produto
from datetime import datetime

class InicioView(LoginRequiredMixin, TemplateView):
    template_name = "paginas/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["clientes"] = Cliente.objects.filter(criado_em__month=datetime.now().month).count()
        context["pedidos"] = Pedido.objects.filter(criado_em__month=datetime.now().month).count()
        context["produtos"] = Produto.objects.filter(criado_em__month=datetime.now().month).count()

        return context


class SobreView(LoginRequiredMixin, TemplateView):
    template_name = "paginas/sobre.html"
