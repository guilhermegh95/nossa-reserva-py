from django.contrib import admin
from .models import Usuario, AreaComum, AreaLocacao, Condominio


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'apartamento')

@admin.register(AreaComum)
class AreaComumAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id')

@admin.register(AreaLocacao)
class AreaLocacaoAdmin(admin.ModelAdmin):
    list_display = ('nome_pessoa', 'area_comum', "data")

@admin.register(Condominio)
class CondominioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id')



# Register your models here.
