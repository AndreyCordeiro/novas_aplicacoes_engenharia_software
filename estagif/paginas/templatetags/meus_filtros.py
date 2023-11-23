from django import template

register = template.Library()


@register.filter(name="valor_total_item_carrinho")
def valor_total_item_carrinho(quantidade, valor):
    return quantidade * valor


# @register.simple_tag(name="valor_total_pedido")
# def valor_total_pedido(obj):
#     return
