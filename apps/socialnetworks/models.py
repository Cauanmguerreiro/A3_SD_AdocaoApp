from django.db import models

# Create your models here.
class Socialnetwork(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição', max_length=100, blank=True, null=True) # Corrigido 'Descricao' e tornado opcional
    url_prefix = models.CharField('Prefixo da URL (ex: https://twitter.com/)', max_length=200, blank=True, null=True)
    icon_class = models.CharField('Classe do Ícone (ex: fab fa-twitter)', max_length=50, blank=True, null=True) # Para ícones em um frontend
    
    class Meta:
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'
        ordering =['id']

    def __str__(self):
        return self.name
