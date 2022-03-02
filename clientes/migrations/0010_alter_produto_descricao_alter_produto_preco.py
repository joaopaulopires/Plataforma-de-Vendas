# Generated by Django 4.0 on 2022-03-02 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_remove_person_dt_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.CharField(max_length=200, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço'),
        ),
    ]
