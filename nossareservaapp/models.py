from django.db import models

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True
        

class Usuario(Base):
    email = models.EmailField(max_length=254)
    apartamento = models.CharField(max_length=10, primary_key=True)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
    def __str__(self):
        return self.apartamento
     

class Condominio(Base):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=254)
    logo = models.URLField
    
    class Meta:
        verbose_name = 'Condominio'
     
    def __str__(self):
        return self.nome


class AreaComum(Base):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=254)
    foto = models.URLField
    
    class Meta:
        verbose_name = 'Area Comum'
        verbose_name_plural = 'Areas comuns'
    
    def __str__(self):
        return self.nome


class AreaLocacao(Base):
    id = models.AutoField(primary_key=True)
    nome_pessoa = models.ForeignKey(Usuario, related_name='locacoes', on_delete=models.CASCADE)
    area_comum = models.ForeignKey(AreaComum, on_delete=models.CASCADE)
    data = models.DateField()

    class Meta:
        verbose_name = 'Locação'
        verbose_name_plural = 'Locações'
        unique_together = ['area_comum', 'data']

    def __str__(self):
        return f'{self.nome_pessoa} alugou a area comum {self.area_comum} para o dia {self.data}'