from django.urls import path

from .views import UsuarioAPIView, AreaComumAPIView, AreaLocacaoAPIView, UsuariosAPIView, AreasComunsAPIView, AreaLocacoesAPIView, CondominioAPIView, CondominiosAPIView


urlpatterns = [
    path('usuarios/', UsuariosAPIView.as_view(), name='usuarios'),
    path('areascomuns/', AreasComunsAPIView.as_view(), name='areacomum'),
    path('locacoes', AreaLocacoesAPIView.as_view(), name='locacoes'),
    path('usuarios/<int:pk>/', UsuarioAPIView.as_view(), name='usuarios'),
    path('areascomuns/<int:pk>/', AreaComumAPIView.as_view(), name='areacomum'),
    path('locacoes/<int:pk>/', AreaLocacaoAPIView.as_view(), name='locacoes'),
    path('condominio/<int:pk>/', CondominioAPIView.as_view(), name='condominio'),
    path('condominio', CondominiosAPIView.as_view(), name='locacoes'),
]