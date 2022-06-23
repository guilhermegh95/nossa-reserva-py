from rest_framework import serializers

from .models import Usuario, AreaLocacao, AreaComum, Condominio


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


class UsuarioSerializer(serializers.ModelSerializer):
    #HyperLinked Related Field
    locacoes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='arealocacao-detail'
    )

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

    def create(self, validated_data):
        user = Usuario.objects.create_user(validated_data['username'], validated_data["password"])
        return user



class CondominioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Condominio
        fields = '__all__'