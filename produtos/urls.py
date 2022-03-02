from django.urls import path
from .views import lista_produtos, produto_detalhado, novo_produto, atualizar_produto, deletar_produto

urlpatterns = [
    path('', lista_produtos.as_view(), name="lista_produtos"),
    path('cadastro/<int:pk>/', produto_detalhado.as_view(), name="produto_detalhado"),
    path('novo/', novo_produto.as_view(), name="novo_produto"),
    path('atualizar/<int:pk>/', atualizar_produto.as_view(), name="atualizar_produto"),
    path('deletar/<int:pk>/', deletar_produto.as_view(), name="deletar_produto"),
]
