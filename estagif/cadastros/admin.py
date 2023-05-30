from django.contrib import admin
from .models import Marca, Produto, Cliente, Pedido, Pagamento, ProdutoPedido, Carrinho

# Register your models here.

admin.site.register(Marca)
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Pagamento)
admin.site.register(ProdutoPedido)
admin.site.register(Carrinho)
