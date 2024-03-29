# Generated by Django 4.1.5 on 2023-05-29 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cadastros", "0007_itemcarrinho_carrinho"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProdutoPedido",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "preco",
                    models.DecimalField(
                        decimal_places=2, max_digits=9, verbose_name="Preço"
                    ),
                ),
                ("quantidade", models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name="carrinho",
            name="itens",
        ),
        migrations.RemoveField(
            model_name="carrinho",
            name="usuario",
        ),
        migrations.RemoveField(
            model_name="pedido",
            name="produtos",
        ),
        migrations.AddField(
            model_name="carrinho",
            name="produto",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="cadastros.produto",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="carrinho",
            name="quantidade",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="pedido",
            name="preco",
            field=models.DecimalField(
                decimal_places=2, default=0.0, max_digits=9, verbose_name="Preço"
            ),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="ItemCarrinho",
        ),
        migrations.AddField(
            model_name="produtopedido",
            name="pedido",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cadastros.pedido"
            ),
        ),
        migrations.AddField(
            model_name="produtopedido",
            name="produto",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cadastros.produto"
            ),
        ),
    ]
