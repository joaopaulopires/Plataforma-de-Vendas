from django.urls import path
from .views import lista_clientes, novo_cliente, atualizar_cliente, deletar_cliente


urlpatterns = [
    path('lista/', lista_clientes, name='lista_clientes'),
    path('novo/', novo_cliente, name="novo_cliente"),
    path('update/<int:id>/', atualizar_cliente, name="atualizar_cliente"),
    path('delete/<int:id>/', deletar_cliente, name="deletar_cliente"),
]
