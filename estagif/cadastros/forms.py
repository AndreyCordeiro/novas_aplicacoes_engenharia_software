from dal import autocomplete
from django import forms
from .models import Pedido


class PedidoForms(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["ciclo", "cliente"]
        widgets = {
            'cliente': autocomplete.ModelSelect2(
                url='buscar-cliente',
                attrs={
                    'data-placeholder': 'Informe o nome do Cliente...',
                    'data-minimum-input-length': 3,
                },
            )
        }
