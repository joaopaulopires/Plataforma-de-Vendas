from django.shortcuts import render
from .models import Produto
from .forms import ProdutoForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


class lista_produtos(ListView):
    model = Produto

class produto_detalhado(DetailView):
    model = Produto

class novo_produto(CreateView):
    model = Produto
    fields = ['name', 'quant', 'preco', 'descricao']
    success_url = reverse_lazy('lista_produtos')

class atualizar_produto(UpdateView):
    model = Produto
    fields = ['name', 'quant', 'preco', 'descricao']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('lista_produtos')

class deletar_produto(DeleteView):
    model = Produto

    def get_success_url(self):
        return reverse_lazy('lista_produtos')

# Documentação Class Based View
# https://docs.djangoproject.com/en/4.0/topics/class-based-views/
# https://docs.djangoproject.com/en/4.0/ref/class-based-views/
# https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/
# https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-editing/
# https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-display/
#
# Create your views here.

