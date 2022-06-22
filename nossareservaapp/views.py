from rest_framework import authentication, permissions

from rest_framework import generics

from .models import Usuario, AreaComum, AreaLocacao, Condominio
from .serializers import UsuarioSerializer, AreaComumSerializer, AreaLocacaoSerializer, CondominioSerializer

authentication_classes = [authentication.TokenAuthentication, ]
permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

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


class AreaLocacoesAPIView(generics.ListCreateAPIView):
    queryset = AreaLocacao.objects.all()
    serializer_class = AreaLocacaoSerializer


class CondominioAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer


class CondominiosAPIView(generics.ListCreateAPIView):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer