from django.db import models
from django.utils import timezone


class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc

class Person(models.Model):
    first_name = models.CharField(verbose_name="Nome", max_length=100)
    last_name = models.CharField(verbose_name="Sobrenome", max_length=100)
    age = models.IntegerField(verbose_name="Idade", null=True, blank=True)
    dt_nasc = models.DateField(verbose_name="Data de Nascimento", default=timezone.now)
    salary = models.DecimalField(verbose_name="Renda", max_digits=7, decimal_places=2, null=True, blank=True)
    bio = models.TextField(verbose_name="Sobre")
    photo = models.ImageField(verbose_name="Foto", upload_to='cliente_foto', null=True, blank=True)
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Produto(models.Model):
    descricao = models.CharField(verbose_name="Descrição", max_length=200)
    preco = models.DecimalField(verbose_name="Preço", max_digits=8, decimal_places=2)

    def __str__(self):
        return self.descricao

class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    imposto = models.DecimalField(max_digits=5, decimal_places=2)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto, related_name="vendas", through="ProdutoVenda")

    def __str__(self):
        return self.numero

class ProdutoVenda(models.Model):
    numero = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name="produto_venda")
    descricao = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="produto_venda")
    desconto_p = models.IntegerField()

    def __str__(self):
        return "{} - {} ({})".format(self.descricao, self.numero, self.desconto_p)




# Create your models here.
