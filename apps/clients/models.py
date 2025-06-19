from django.db import models
# Importe o modelo de "Socialnetwork" depois do "from django.db import models" para
# adicionar o relacionamento da chave estrangeira indicando a propriedade
# do modelo ao socialnetworks criado.
from apps.socialnetworks.models import Socialnetwork # Ajustado o caminho do import

# Create your models here.
class Client(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100)
    address = models.CharField('Endereco', max_length=200)
    cell_phone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    socialnetwork = models.ManyToManyField(Socialnetwork, verbose_name="Redes Sociais") # O nome do campo é 'socialnetwork', mas geralmente se usa plural para ManyToManyField, como 'socialnetworks'

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.first_name
