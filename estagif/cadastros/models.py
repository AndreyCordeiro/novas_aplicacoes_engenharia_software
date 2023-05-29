from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Marca(models.Model):
    nome = models.CharField(max_length=55)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=55)
    preco = models.DecimalField(
        decimal_places=2, max_digits=9, verbose_name="Preço")
    codigo = models.IntegerField(verbose_name="Código")
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, help_text="Selecione a Marca")

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Nome: {self.nome} | R${self.preco} | Código: {self.codigo} | Marca: {self.marca.nome}"


class Cliente(models.Model):
    nome = models.CharField(max_length=55)
    cpf = models.CharField(max_length=14, verbose_name="CPF", unique=True)
    telefone = models.CharField(max_length=15)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Nome: {self.nome} | CPF: {self.cpf} | Telefone: {self.telefone}"


class Pedido(models.Model):
    produtos = models.ForeignKey(
        Produto, on_delete=models.PROTECT, help_text="Selecione um Produto")
    ciclo = models.IntegerField(verbose_name="Ciclo")
    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT, help_text="Selecione um Cliente")

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)


class Pagamento(models.Model):
    valor_recebido = models.DecimalField(
        decimal_places=2, max_digits=9, verbose_name="Valor Recebido")
    valor_parcela = models.DecimalField(
        decimal_places=2, max_digits=9, verbose_name="Valor da Parcela")
    data_vencimento = models.DateField()
    data_pagamento = models.DateField()
    parcelas = models.IntegerField(verbose_name="Parcelas")
    forma_pagamento = models.CharField(
        max_length=55, verbose_name="Forma pagamento")

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
