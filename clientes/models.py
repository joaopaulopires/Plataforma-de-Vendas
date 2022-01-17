from django.db import models

class Person(models.Model):
    first_name = models.CharField(verbose_name="Nome", max_length=100)
    last_name = models.CharField(verbose_name="Sobrenome", max_length=100)
    age = models.IntegerField(verbose_name="Idade")
    salary = models.DecimalField(verbose_name="Renda", max_digits=7, decimal_places=2, null=True, blank=True)
    bio = models.TextField(verbose_name="Sobre")
    photo = models.ImageField(verbose_name="Foto", upload_to='cliente_foto', null=True, blank=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name



# Create your models here.
