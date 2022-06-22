from rest_framework import serializers

from .models import Usuario, AreaLocacao, AreaComum

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kargs = {
            'email': {'write_only': True}
        }
        model = Usuario
        """
        fields = {
            'apartamento',
        }"""
        fields = '__all__'

class AreaComumSerializer(serializers.ModelSerializer):

    class Meta:
        model = AreaComum
        """
        fields = {
            'id',
            'nome',
        }"""
        fields = '__all__'

class AreaLocacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AreaLocacao
        """
        fields = {
            'id',
            'nome_pessoa',
            'area_comum',
            'data',
        }"""
        fields = '__all__'