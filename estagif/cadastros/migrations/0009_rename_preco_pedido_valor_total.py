# Generated by Django 4.1.5 on 2023-05-30 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cadastros", "0008_produtopedido_remove_carrinho_itens_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pedido",
            old_name="preco",
            new_name="valor_total",
        ),
    ]
