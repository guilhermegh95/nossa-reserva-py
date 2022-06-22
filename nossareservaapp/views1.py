from rest_framework import authentication, permissions

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario, AreaComum, AreaLocacao
from .serializers import UsuarioSerializer, AreaComumSerializer, AreaLocacaoSerializer

authentication_classes = [authentication.TokenAuthentication, ]
permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class UsuarioAPIView(APIView):
    """
    API de Usuario
    """
    def get(self, request):
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AreaComumAPIView(APIView):
    """
    API de AreaComum
    """
    def get(self, request):
        areacomum = AreaComum.objects.all()
        serializer = AreaComumSerializer(areacomum, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AreaComumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class AreaLocacaoAPIView(APIView):
    """
    API de Locacao
    """
    def get(self, request):
        arealocacao = AreaLocacao.objects.all()
        serializer = AreaLocacaoSerializer(arealocacao, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AreaLocacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



