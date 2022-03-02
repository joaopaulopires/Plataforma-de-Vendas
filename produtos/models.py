from django.db import models

class Produto(models.Model):
    name = models.CharField(verbose_name="Nome do Produto", max_length=100)
    quant = models.IntegerField(verbose_name="Quantidade", default=0)
    preco = models.DecimalField(verbose_name="Preço", max_digits=8, decimal_places=2)
    descricao = models.CharField(verbose_name="Descrição", max_length=200)

    def __str__(self):
        return self.name +' / '+str(self.quant)

# Create your models here.
