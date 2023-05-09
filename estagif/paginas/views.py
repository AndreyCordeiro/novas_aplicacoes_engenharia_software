from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class InicioView(LoginRequiredMixin, TemplateView):
    template_name = "paginas/index.html"


class SobreView(LoginRequiredMixin, TemplateView):
    template_name = "paginas/sobre.html"
