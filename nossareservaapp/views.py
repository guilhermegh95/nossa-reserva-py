from rest_framework import authentication, permissions

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import permissions

from .models import Usuario, AreaComum, AreaLocacao, Condominio
from .serializers import UsuarioSerializer, AreaComumSerializer, AreaLocacaoSerializer, CondominioSerializer

authentication_classes = [authentication.TokenAuthentication, ]
permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

"""
API V1
"""

class UsuarioAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuariosAPIView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class AreaComumAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AreaComum.objects.all()
    serializer_class = AreaComumSerializer


class AreasComunsAPIView(generics.ListCreateAPIView):
    queryset = AreaComum.objects.all()
    serializer_class = AreaComumSerializer


class AreaLocacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AreaLocacao.objects.all()
    serializer_class = AreaLocacaoSerializer

    def get_object(self):
        if self.kwargs.get('usuario_pk'):
            return get_object_or_404(self.get_queryset(), nome_pessoa=self.kwargs.get('nome_pessoa'), pk=self.kwargs.get('locacoes_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('locacoes_pk'))


class AreaLocacoesAPIView(generics.ListCreateAPIView):
    queryset = AreaLocacao.objects.all()
    serializer_class = AreaLocacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('usuario_pk'):
            return self.queryset.filter(nome_pessoa=self.kwargs.get('usuario_pk'))
        return self.queryset.all()


class CondominioAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer


class CondominiosAPIView(generics.ListCreateAPIView):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer


"""
API V2
"""
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @action(detail=True, methods=['get'])
    def locacoes(self, request, pk=None):
        nome_pessoa = self.get_object()
        serializer = AreaLocacaoSerializer(nome_pessoa.locacoes.all(), many=True)
        return Response(serializer.data)


class AreaComumViewSet(viewsets.ModelViewSet):
    queryset = AreaComum.objects.all()
    serializer_class = AreaComumSerializer


class AreaLocacaoViewSet(viewsets.ModelViewSet):
    queryset = AreaLocacao.objects.all()
    serializer_class = AreaLocacaoSerializer


class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer

